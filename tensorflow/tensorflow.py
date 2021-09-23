import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestCentroid
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
import string
import re
import spacy
import json
import deephaven.npy as inp
from deephaven.java_to_python import columnToNumpyArray
from deephaven import DynamicTableWriter, Types as dht
from deephaven.TableTools import timeTable

# Load training data to use:
if not "trainData" in globals():
    print("Data not available: please load trainData.csv")

# Ensure credientials are setup to log in to seekingAlpha
if not "ra_sa_key" in globals():
    print("Please set Rapid Api key for Seeking Alpha (ra_sa_key='the-key'):")


def cleanText(text):
    # to lowercase
    text = text.lower()
    # correct spaces (e.g. "End sentence.Begin another" becomes "End sentence. Begin another")
    text = re.sub(r'\.([a-zA-Z])', r'. \1', text)
    text = re.sub(r'\?([a-zA-Z])', r'. \1', text)
    text = re.sub(r'\!([a-zA-Z])', r'. \1', text)
    # replace q1,2,3,4 with q
    text = re.sub("q[1-4]", "q", text)
    # replace 20xx with 2000
    text = re.sub("20[0-2][0-9]", "2000", text)
    # lemmatize and remove stop words and punctuation
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    lemmatizedText = ""
    for token in doc:
        if not token.is_stop and not token.is_punct:
            lemma = token.lemma_
            if lemma == "-PRON-":
                lemma = "it"
            lemmatizedText += (lemma + " ")
    text = lemmatizedText
    return text


def shuffleTable(unshuffledTable):
    return unshuffledTable.update("__r=Math.random()").sort("__r").dropColumns("__r")


def centroid(trainTextVectorized, trainLabels, testTextVectorized):
    nc = NearestCentroid(metric='manhattan')
    nc.fit(trainTextVectorized, trainLabels)
    return nc.predict(testTextVectorized)


def naiveBayes(trainTextVectorized, trainLabels, testTextVectorized):
    nb = BernoulliNB(alpha=1)
    nb.fit(trainTextVectorized, trainLabels)
    return nb.predict(testTextVectorized)


def preTrainedEmbedding(trainText, trainLabels, evalText, valSize, trainEmb=True):
    # initialize training, validation, and testing data
    valText = trainText[-1 * valSize:]
    valLabels = trainLabels[-1 * valSize:]
    trainText = trainText[:-1 * valSize]
    trainLabels = trainLabels[:-1 * valSize]
    # create and run model
    hub_layer = hub.KerasLayer("https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim-with-oov/1", output_shape=[20],
                               input_shape=[], dtype=tf.string, trainable=trainEmb)
    model = keras.Sequential(name="mymodel")
    model.add(hub_layer)
    model.add(keras.layers.Dense(16, activation='relu'))
    model.add(keras.layers.Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    history = model.fit(trainText,
                        trainLabels,
                        epochs=40,
                        batch_size=4,
                        validation_data=(valText, valLabels),
                        verbose=0)
    model.predict(evalText, verbose=1)


def predict(text, model):
    if model == 'c' or model == 'nb':
        textVectorized = vectorizer.transform([text])
        if model == 'c':
            return int(centroid(trainTextVectorized, trainLabels, textVectorized)[0])
        else:
            return int(naiveBayes(trainTextVectorized, trainLabels, textVectorized)[0])
    elif model == 'e':
        return int(preTrainedEmbedding(trainText, trainLabels, text, 10))


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from deephaven.TableTools import emptyTable
from deephaven.conversion_utils import convertToJavaArray


# gets only those xml items which represent earnings call transcripts
def getEarningsCalls(items):
    return [item for item in items if item.title.text.split()[-3:] == ["Earnings", "Call", "Transcript"]]


# gets the symbol and quarter/year out of an article's header
def parseHeader(header):
    leftParenIdx = header.rindex("(")
    rightParenIdx = header.rindex(")")
    symbol = header[leftParenIdx + 1:rightParenIdx]
    quarterIdx = re.search("Q[1-4] 20[0-2][0-9]", header).start()
    quarter = header[quarterIdx:quarterIdx + 7]
    return (symbol, quarter)


# find the index of the first paragraph that is equal to an item from the search list
# necessary for some functions below
def findIdx(paragraphs, searchList):
    idx = 0
    for paragraph in paragraphs:
        for title in searchList:
            if (title == paragraph.text.lower()):
                return idx
        idx += 1
    return idx


# gets the names of all the company participants on the call
# this is useful in other functions below
def getNames(paragraphs):
    # find the indices of the company participants and conference call participants roll-call sections
    companyList = ["company participants", "corporate participants", "executives", "company representatives"]
    confList = ["conference call participants", "analysts"]
    startIdx = findIdx(paragraphs, companyList)
    endIdx = findIdx(paragraphs, confList)

    # record the name of each company participant
    idx = startIdx + 1
    names = []
    while idx < endIdx:
        paragraph = paragraphs[idx]
        text = paragraph.text.split()
        if len(text) < 2:
            break
        names.append(text[0] + " " + text[1])
        idx += 1
    return names


# removes the roll-call, operator announcement, and q&a sections of the call
def truncate(paragraphs, names):
    # find the indices of the operator and q&a sections
    operatorIdx = qaIdx = 0
    for paragraph in paragraphs:
        if paragraph.text.lower()[:len("operator")] == "operator":
            break
        operatorIdx += 1
    for paragraph in paragraphs:
        if "id" in paragraph.attrs.keys() and paragraph["id"].lower()[:len("question-answer-session")] == "question-answer-session":
            break
        qaIdx += 1

    # if there is an operator section, get the section between it and the q&a
    if operatorIdx < qaIdx:
        paragraphs = paragraphs[operatorIdx + 1:qaIdx - 1]
    # if there isn't an operator section, remove the company participant roll-call
    # this is necessary for the next step
    else:
        confList = ["conference call participants", "analysts"]
        confIdx = findIdx(paragraphs, confList)
        paragraphs = paragraphs[confIdx:qaIdx - 1]

    # find the index of the first company participant's speaking section
    # this represents the start of either the safe-harbor statement or the CEO presentation
    nameIdx = 0
    for paragraph in paragraphs:
        text = paragraph.text.split()
        if len(text) < 2:
            break
        name = text[0] + " " + text[1]
        if name in names:
            break
        nameIdx += 1

    # remove everything before the first company participant's speaking section
    # print("op:%d\nqa:%d\nname:%d" % (operatorIdx, qaIdx, nameIdx))
    return paragraphs[nameIdx:]


# check if the call has a safe-harbor section
def hasSafeHarborStatement(paragraphs):
    phrases = ["10-K", "forward-looking statements", "forward-looking information", "non-GAAP"]
    for paragraph in paragraphs:
        for phrase in phrases:
            if phrase in paragraph.text:
                return True
    return False


# remove the call's safe-harbor section with the assumption that it exists
def removeSafeHarborStatement(paragraphs, names):
    # find the indices of the first two company participant speaking sections
    # the first company speaker always says the safe-harbor statement, so his/her section must be removed
    i = startIdx = endIdx = 0
    first = True
    for paragraph in paragraphs:
        text = paragraph.text.split()
        if text[0].lower() == "presentation":
            i += 1
            continue
        name = text[0] + " " + text[1]
        if name in names:
            if first:
                # this is the first speaker's index
                startIdx = i
                first = False
            else:
                # this is the second speaker's index
                endIdx = i
                break
        i += 1

    # remove the section between the two indices, i.e. the first speaker's section
    return paragraphs[:startIdx] + paragraphs[endIdx + 1:]


# removes all company participant names/paragraphs, as each name has its own paragraph in the call
def removeNames(paragraphs, names):
    return [paragraph for paragraph in paragraphs if not paragraph.text in names]


# convert a list of paragraphs into a single text string
def collate(paragraphs):
    s = ""
    for paragraph in paragraphs:
        s += paragraph.text
    return s


def getArticle(articleId):
    url = "https://seeking-alpha.p.rapidapi.com/articles/get-details"

    querystring = {"id": articleId}

    headers = {
        'x-rapidapi-host': "seeking-alpha.p.rapidapi.com",
        'x-rapidapi-key': ra_sa_key
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


def runRSS():
    # get the rss feed
    feed = requests.get("https://seekingalpha.com/sector/transcripts.xml").text
    soup = BeautifulSoup(feed, "xml")
    items = soup.find_all("item")
    items = getEarningsCalls(items)
    links = [item.link.text for item in items]

    # these store the data for articles where access is granted
    texts = []
    timestamps = []
    symbols = []
    quarters = []
    for link in links[:1]:
        linkId = link[link.index('/article/') + len('/article/'): link.index('-')]

        # Note: every tick, the API request will be re-sent, either consuming quota
        # fast, or racking up bills fast. Skipping already seen links minimizes API
        # usage to only new articles.
        if linkId in knownLinks:
            # print("Skipping lookup - already included: " + link)
            continue
        else:
            knownLinks.append(linkId)

        # get the transcript article
        source = json.loads(getArticle(linkId).text)

        try:
            # find the header, timestamp, and paragraphs of the article
            article = source["data"]["attributes"]["content"]
            header = source["data"]["attributes"]["title"]
            timestamp = source["data"]["attributes"]["publishOn"]
            paragraphs = BeautifulSoup(article, "lxml").find_all("p")

            # get symbol and quarter from the header
            symbol, quarter = parseHeader(header)

            # clean and collate the paragraphs
            names = getNames(paragraphs)
            paragraphs = truncate(paragraphs, names)
            if hasSafeHarborStatement(paragraphs):
                paragraphs = removeSafeHarborStatement(paragraphs, names)
            paragraphs = removeNames(paragraphs, names)
            text = collate(paragraphs)

            # store collected data
            texts.append(text)
            timestamps.append(timestamp)
            symbols.append(symbol)
            quarters.append(quarter)
        except:
            # either bad article or access denied
            print("Warning: article skipped due to bad formatting or access denied.")
            pass

    if len(texts) == 0:
        return False

    # Known bug: https://github.com/deephaven/deephaven-core/issues/1309
    try:
        symCol = columnToNumpyArray(calls, "Sym")
    except:
        symCol = []
    try:
        quarterCol = columnToNumpyArray(calls, "Quarter")
    except:
        quarterCol = []
    containsNewCall = False
    for i in range(len(texts)):
        if symbols[i] not in symCol and quarters[i] not in quarterCol:
            containsNewCall = True
        tw.logRow(texts[i], timestamps[i], symbols[i], quarters[i])
    return containsNewCall


trainData = shuffleTable(trainData)
trainText = columnToNumpyArray(trainData, "Text")
trainLabels = inp.numpy_slice(trainData.view("Label"), 0, trainData.size(), dtype=np.int32)
trainLabels = np.reshape(trainLabels, -1)
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 1), norm='l1')
trainTextVectorized = vectorizer.fit_transform(trainText)

knownLinks = []
cols = ["Text", "RSSTimestamp", "Sym", "Quarter"]
types = [dht.string, dht.string, dht.string, dht.string]
tw = DynamicTableWriter(cols, types)
twt = tw.getTable()
calls = twt \
    .firstBy("Sym", "Quarter") \
    .update("Text = (String)cleanText.call(Text)", "PredictedLabel = (int)predict.call(Text, `c`)", "PredictedLabel = PredictedLabel==0 ? -1 : PredictedLabel") \
    .moveUpColumns("Sym", "Quarter", "RSSTimestamp", "PredictedLabel")

tt = timeTable("'00:01:00'") \
    .sortDescending("Timestamp") \
    .update("ContainedNewCalls=(boolean)runRSS.call()")
callsSummary = calls.view("Sym", "Date=convertDate(RSSTimestamp.substring(0,10))", "PredictedLabel")
