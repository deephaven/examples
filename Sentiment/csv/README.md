# Sentiment dataset

## This folder contains a single file:

- `sentiment.csv`

## About the file

This file contains data pertaining to the GOP debate that took place on August 6, 2015 in Cleveland, Ohio.  The debate lasted two hours, and invited the 10 most candidates atop the polls at the time.  The file `sentiment.csv` contains information about 13,871 unique tweets related to this debate.  The parameters of each tweet (columns in the file) are as follows:

- `id`
- `candidate`
- `candidate_confidence`
- `relevant_yn`
- `relevant_yn_confidence`
- `sentiment`
- `sentiment_confidence`
- `subject_matter`
- `subject_matter_confidence`
- `candidate_gold`
- `name`
- `relevant_yn_gold`
- `retweet_count`
- `sentiment_gold`
- `subject_matter_gold`
- `text`
- `tweet_coord`
- `tweet_created`
- `tweet_id`
- `tweet_location`
- `user_timezone`

Many of these fields are in string format.  Thus, this dataset can be used for textual data handling in Deephaven, sentiment analysis, etc.

# Source and Licence

This dataset is publicly available on [Kaggle](https://www.kaggle.com/) at [this url](https://www.kaggle.com/crowdflower/first-gop-debate-twitter-sentiment).

The data is licensed under the Creative Commons public domain CC BY-NC-SA 4.0.  Deephaven makes no claim of its authenticity or its accuracy.  It has been placed here for demonstrative purposes.