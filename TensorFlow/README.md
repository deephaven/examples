# Tensorflow example demonstrating data from Seeking Alpha

Pull a RSS feed from Seeking Alpha, and statistically calculate positive/negative sentiment using machine-learning
training mechanisms within [TensorFlow](https://www.tensorflow.org/).

## Table of contents

* `tensorflow.py` - Python script to run.
* `trainData.csv` - The input data to train the AI algorithm.

## Steps to run

1. Install Python modules:
   `docker exec $(basename $(pwd))_grpc-api_1 pip install tensorflow tensorflow_hub sklearn spacy bs4 lxml`
   Note: please use this exact install mechanism, rather than variations
   from [How to install Python packages](https://deephaven.io/core/docs/how-to-guides/install-python-packages).
   The lxml installation is somewhat fragile in allowing bs4 to see that it has been installed. 
   See <https://github.com/deephaven/deephaven-core/discussions/1299> for more information.
1. Install the spacy english module:
   `docker exec $(basename $(pwd))_grpc-api_1 pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz`
   Alternatively, use another version from here:
   <https://github.com/explosion/spacy-models/releases/>
1. Drag/drop the file `trainData.csv` onto the Deephaven console.
1. Get a login to <https://rapidapi.com/developer> (free) and subscribe to <https://rapidapi.com/apidojo/api/seeking-alpha/>.
    * Note that every time you run the script, you will consume some quota of your API usage for this particular
      endpoint. This is kept minimal: a single API access of each published article being advertised by Seeking Alpha
      on any one day (using the `knownLinks[]` variable within the script). However, to allow repeated iterations for
      debug/troubleshooting, all variables are reset on a new script run, and hence another round of API calls is
      required for each run.
    * The number of API calls per day is usually small(~5-30), so provided the script is only run once-per-day, the free
      tier of 500 calls/month should be adequate for demonstrative purposes.
    * API call usage can be seen here: <https://rapidapi.com/developer/dashboard>
1. Look at any of the endpoint examples, and **select+save** your unique endpoint API key. It is called `x-rapidapi-key`.
1. Import your key into Deephaven by running: 
  `ra_sa_key='enter-your-key-here'` (avoiding any additional space/quote characters)
1. Run `tensorflow.py`.
