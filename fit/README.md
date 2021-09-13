# Fit file as available from Strava

Pull your own data from your Strava account. Visualize, manipulate, and combine your data with other sources, all while maintaining full ownership and control of the data in your own environment.

## Table of contents

 * `ThursMorn.fit` - The data used to run this example.
 * `accessFit.py` - Python script to demonstrate fit data inside Deephaven. 
 * `*.png` - Images used in this help.

## Steps to run

These steps can be run with our example data or your own.

1. Login to your Strava account.
1. Select an activity.
1. At the bottom of the menu, select **...** for more.
   ![Strava export menu](StravaExport.png "Strava export menu")
1. Select **Export Original**. Provided you have supplied the data in fit format, this should now give a downloaded file with extension `.fit`
1. Put this `.fit` file in the data folder underneath your Docker starting location:
   See: https://deephaven.io/core/docs/tutorials/launch-pre-built#set-up-your-deephaven-deployment
   Add another directory level if desired to keep various projects segmented.
1. Ensure fitparse is setup (see below).
1. Run the given file in a Deephaven console: `accessFit.py`.
1. The `heartRateData` table should appear.
   ![Heart rate table](heartRateTable.png "Heart rate table")
1. Click the hamburger menu in the `heartRateData` tab.
1. Select `Chart Builder`
1. Select defaults (`Line`, `X-Axis=Timestamp`, `Series=Heart Rate`)
1. Press **Create** (note: you may need to scroll to see the button.)
1. A chart should appear:
   ![Heart rate chart](heartRateChart.png "Heart rate chart")

## Using fitparse module
To use fitparse, install via your python session temporarily using:
```python
import os
os.system("pip install fitparse")
```
For more details on making the install persist between sessions, see [How to install Python packages](https://github.com/deephaven/deephaven.io/blob/main/core/docs/how-to-guides/install-python-packages.md).
https://github.com/deephaven/deephaven.io/blob/main/core/docs/how-to-guides/install-python-packages.md

Note: YMMV if using a fit file which reports different data types. It appears that different sensors can report different data. In the example here, both GPS and heart rate monitor data is intertwined.

## Advanced challenge

Some of the most interesting use cases for this data are to be able to correlate the data with other sources of interest to you.

The first step is importing many fit files to compare:

* Today's heart rate with last month's heart rate.
* average heart rate last week/month
* heart rate at different points during the day (morning, lunch, bedtime)
* correlate live heart rate data, with past heart rate data from your fit files: see`tickingHeartRate` for ideas on getting started with live heart rate data.

For more insight, correlate this data with:
* diet macro nutrients - do you run faster when you have more protein?
* sleep patterns - is heart rate affected by the amount of sleep you have had?
* weather (temperature, wind chill, humidity)
* confirming health improvements - do you see positive gains in heart health over time

# Source and License

This data was contributed to the public domain by the author. It is provided here for demonstrative purposes without any warranty for fitness of purpose or usability.
