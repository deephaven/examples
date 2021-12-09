# Fit file as available from Strava

Pull your own data from your [Strava](https://www.strava.com/) account. Visualize, manipulate, and combine your data with other sources, all while maintaining full ownership and control of the data in your own environment.

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
1. Select **Export Original**. Provided you have supplied the data in fit format, this should now give a downloaded file with the `.fit` extension.
1. Put this `.fit` file in the data folder underneath your Docker starting location:
   See our [Quickstart](https://deephaven.io/core/docs/tutorials/quickstart/#set-up-your-deephaven-deployment) for more information.
   Add another directory level if desired to keep various projects segmented.
1. Ensure fitparse is setup (see [below](#using-fitparse-module)).
1. Run the `accessFit.py` file in a Deephaven console.
1. The `heart_rate_data` table should appear.

   ![heart_rate_data](heartRateTable.png "heart_rate_data")
1. Click the **Table Options** menu in the `heart_rate_data` tab.
1. Select **Chart Builder**.
1. Select defaults: `Line`, `X-Axis=Timestamp`, `Series=HeartRate`
1. Press **Create** (note: you may need to scroll to see the button.)
1. A chart should appear:

   ![heart_rate_data](heartRateChart.png "heart_rate_data")

## Using fitparse module

To use fitparse, install via your current Python session:

```python
import os
os.system("pip install fitparse")
```

For more details on making the install persist between sessions, see [How to install Python packages](https://github.com/deephaven/deephaven.io/blob/main/core/docs/how-to-guides/install-python-packages.md).

Note: Your mileage may vary if using a `.fit` file which reports different data types. Different sensors can report different data. In the example here, both GPS and heart rate monitor data is intertwined.

## Advanced challenge

Some of the most interesting use cases for this data are to correlate the data with other sources of interest to you.

The first step is importing many `.fit` files to compare:

- Today's heart rate with last month's heart rate.
- Average heart rate last week/month.
- Heart rate at different points during the day (morning, lunch, bedtime).
- Correlate live heart rate data with past heart rate data from your `.fit` files: see [`tickingHeartRate`](../tickingHeartRate/README.md) for ideas on getting started with live heart rate data.

For more insight, correlate this data with:

- diet macro nutrients - do you run faster when you have more protein?
- sleep patterns - is heart rate affected by your amount of sleep?
- weather - temperature, wind chill, humidity, etc.
- health improvements - do you see positive gains in heart health over time?

# Source and License

This data was contributed to the public domain by the author. It is provided here for demonstrative purposes without any warranty for fitness of purpose or usability.
