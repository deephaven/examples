# Ticking Heart Rate in Deephaven

Self-contained example code and data to simulate a live feed of heart rate data being entered.

## Table of contents

 * `csv` - the data used to run this example
 * `runTickingHeartRateReplay.py` - python script to demonstrate fit data inside deephaven 
 * `*.png` - images used in this help

## Steps to run

1. Copy the `csv` directory into the data folder underneath your Docker starting location. See our [Quick start](https://deephaven.io/core/docs/tutorials/quickstart/#manage-the-deephaven-deployment) for detailed instructions.
1. Run the `runTickingHeartRateReplay.py` file in a Deephaven console.
1. The table `heartRateData` should appear. See: [Note regarding ticking](#note-regarding-ticking).

   ![Heart rate table starting](heartRateTableStart.png "Heart rate chart")   

The table should continue to tick new rows as each `.csv` file is processed.
1. Click the **Table Options** menu in the `heartRateData` tab.
1. Select **Chart Builder**.
1. Select defaults:`Line`, `X-Axis=Timestamp`, `Series=Heart Rate`
1. Select **Create**. (You may need to scroll to see the button.)
1. A chart should appear:

   ![Heart rate chart started](heartRateChartStart.png "Heart rate chart started")

The chart should also continue to tick, adding more data points to the graph over time and dynamically resizing.

   ![Heart rate chart ticking](heartRateChartMiddle.png "Heart rate chart")

The chart will stop ticking when either no more data is added, or the script exit criteria is reached.

   ![Heart rate chart complete](heartRateChartEnd.png "Heart rate chart complete")

## Note regarding ticking

The ticking functionality requires threading to be in place as implemented in the code example.

Without threading, ticking will not happen, and the entire table will be processed in a single batch at the end.

More background detail is supplied here in our guide, [Write data to a real-time table](https://deephaven.io/core/docs/reference/table-operations/create/DynamicTableWriter)

## Advanced challenge

Provided there is a way to stream `.csv` files into the Docker container from the original source, it is possible to watch heart rate monitor data in real-time (however, there may be delays depending on the speed of data transfer protocols).

Since there is a diverse array of devices and communication strategies between those devices, we do not recommended a specific setup here on how to achieve this goal.

For this exercise, the following were used:

- a Scosche Rhythm24 heart rate monitor.
- an Android phone with USB tethering for file sharing (alternatively, syncing software could be used).
- the Strava android app for a clear screen reading of approximately once per-second heart rate readouts.
- the Tasker android app to screen scrape the screen and write a new `.csv` file approximately once per second.

# Source and License

This data was contributed to the public domain by the author. It is provided here for demonstrative purposes without any warranty for fitness of purpose or usability.
