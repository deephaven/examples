# Tensorflow example demonstrating data from Seeking Alpha

Pull a RSS feed from Seeking Alpha, and statistically calculate positive/negative sentiment using machine-learning training mechanisms.

## Table of contents
* `tensorflow.py` - python script to run
* `trainData.csv` - the input data to train the AI algorithm

## Known issues:
TODO: remove/fix this entire section - the example is not usable while these problems exist
1. Without a login to Seeking Alpha, the data will not populate (I believe). That, or the article formatting is potentially fragile.
   * Due to this, I have not been able to run with actual data, to see if/where/how to tie together DynamicTableWriter with the trained system
1. Some fragility in the lxml install within docker/deephaven (See setup) Resolution: https://github.com/deephaven/deephaven.io/pull/608
1. Preemptive updates does not appear to be implemented/supported in core. If this is an essential piece of functionality, still need an alternative.

## Steps to run
1. Install python modules
   `docker exec $(basename $(pwd))_grpc-api_1 pip install tensorflow tensorflow_hub sklearn spacy bs4 lxml`
   Note: please use this exact install mechanism, rather than variations from https://deephaven.io/core/docs/how-to-guides/install-python-packages
   The lxml installation is somewhat fragile in allowing bs4 to see that it has been installed.
1. Drag/drop the file trainData.csv onto the Deephaven console.
1. Run `tensorflow.py`




