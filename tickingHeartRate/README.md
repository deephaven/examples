# Ticking Heart Rate in Deephaven

Self-contained example code and data to simulate a live feed of heart rate data being entered.

## Table of contents

 * `csv` - the data used to run this example
 * `runTickingHeartRateReplay.py` - python script to demonstrate fit data inside deephaven 
 * `*.png` - images used in this help

## Steps to run

1. Copy the `csv` directory into the data folder underneath your docker starting location:
   See: https://deephaven.io/core/docs/tutorials/launch-pre-built#set-up-your-deephaven-deployment
1. Run the file given in a deephaven console: `runTickingHeartRateReplay.py`
1. The table `heartRateData` should appear (See `Note regarding Ticking`)
   ![Heart rate table starting](heartRateTableStart.png "Heart rate chart")   
1. The table should continue to tick new rows as each `.csv` file is processed.
1. Click the hamburger menu in the `heartRateData` tab.
1. Select `Chart Builder`
1. Select defaults (`Line`, `X-Axis=Timestamp`, `Series=Heart Rate`)
1. Press Create (You may need to scroll to see the button.)
1. A chart should appear
   ![Heart rate chart started](heartRateChartStart.png "Heart rate chart started")
1. The chart should also continue to tick, adding more data points to the graph over time and dynamically resizing.
   ![Heart rate chart ticking](heartRateChartMiddle.png "Heart rate chart")
1. The chart will stop ticking when either no more data is added, or the script exit criteria is reached.
   ![Heart rate chart complete](heartRateChartEnd.png "Heart rate chart complete")

## Note regarding ticking

The ticking functionality requires threading to be in place as implemented in the code example.

Without threading, ticking will not happen, and the entire table will be processed in a single batch at the end.

More background detail is supplied here: https://deephaven.io/core/docs/reference/table-operations/create/DynamicTableWriter

## Advanced challenge

Provided there is a way to stream csv files into the docker container from the original source, it should be possible to watch heart rate monitor data in real-time (delays only depending on the speed of data transfer protocols).

Since there is a diverse array of devices and communication strategies between those devices, there is no recommended setup here on how to achieve this goal.

For this exercise, the following were used:
* a Scosche Rhythm24 heart rate monitor
* android phone with USB tethering for file sharing (alternatively syncing software could be used)
* Strava android app for a clear screen reading of per-second(approx.) heart rate readouts
* Tasker android app to screen scrape the screen and write a new csv file ~once per second.

# Source and License

This data was contributed to the public domain by the author. It is provided here for demonstrative purposes without any warranty for fitness of purpose or usability.
