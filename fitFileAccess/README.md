# Fit file as available from Strava

This folder contains

## Table of contents

 * `ThursMorn.fit` - the data used to run this example
 * `accessFit.py` - python script to demonstrate fit data inside deephaven 
 * `*.png` - images used in this help

## Steps to run: example or your own data

1. Login to your Strava account
1. Select an activity.
1. At the bottom of the menu, select the `...` for more
![Strava export menu](StravaExport.png "Strava export menu")
1. Select `Export Original`. Provided you have supplied the data in fit format, this should now give a downloaded file with extension `.fit`
1. Put this `.fit` file in the data folder underneath your docker starting location:
   See: https://deephaven.io/core/docs/tutorials/launch-pre-built#set-up-your-deephaven-deployment
   Add another directory level if desired to keep segmented.
1. Ensure fitparse is setup
1. Run the file given in a deephaven console: `accessFit.py`
1. The table `heartRateData` should appear

<<insert screenshot here>>
![Heart rate table](heartRateTable.png "Heart rate table")

1. Click the hamburger menu in the `heartRateData` tab.
1. Select defaults (`Line`, `X-Axis=Timestamp`, `Series=Heart Rate`)
1. Press Create
1. A chart should appear

![Heart rate chart](heartRateChart.png "Heart rate chart")

## Using fitparse module
To use fitparse, install via your python session temporarily using:
```python
import os
os.system("pip install fitparse")
```
For more details on making the install persist between sessions, see:
https://github.com/deephaven/deephaven.io/blob/main/core/docs/how-to-guides/install-python-packages.md

Note: YMMV if using a fit file which reports different data types. It appears that different sensors can report different data. In the example here, both GPS and heart rate monitor data is intertwined.

# Source and License

This data was contributed to the public domain by the author. It is provided here for demonstrative purposes without any warranty for fitness of purpose or usability.
