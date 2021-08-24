# PeMS example data

This folder contains data files concerning [Caltrans Performance Measurement System (PeMS)](https://pems.dot.ca.gov/) traffic flow.
These partitioned Parquet files are provided by [Clark Fitzgerald](https://anson.ucdavis.edu/~clarkf/) and show the ability to read such structured files in Deephaven Community Core.

The data represents aggregate traffic flow collected every 30 seconds from raw sensors on the three lanes of traffic, from January to October 2016, for a location of the I-80 corridor near Davis, CA.

PeMS computes performance measures from sensor measurements of vehicle count (flow), occupancy, and speed automatically collected on the freeway.
- Occupancy is a measure of how much of the roadway is covered by vehicles.  
- A related quantity is the freeway density, measured in vehicles per mile.
In this location there are only three lanes so only three sensors of information are provided. Lanes 5-8 are present in the `_meta_common` to facilitate importing other locations into the dataset.

## Table of contents

- `parquet`: Directory containing partitioned Parquet data.
- `_common_metadata`: File contains the schema for the whole dataset, including those hierarchical columns and those not in this specific section of the data.
- `_metadata`: File contains the schema used for part files (omitting the hierarchical columns) and per-file column stats (min, max, etc.,) for all the files, with their complete relative path names.

## Fields

  - **timeperiod (String):**  Date and time value for the sample period.
  - **flow1 (int):**  The number of vehicles observed in lane 1 for the sample period.
  - **occupancy1 (double):** The fraction of each sample period during which the detector in lane 1 output is “1”.
  - **speed1 (double):**  The average speed of vehicles in lane 1 during the sample period.
  - **flow2 (int):**  The number of vehicles observed in lane 2 for the sample period.
  - **occupancy2 (double):** The fraction of each sample period during which the detector in lane 2 output is “1”.
  - **speed2 (double):**  The average speed of vehicles in lane 2 during the sample period.
  - **flow3 (int):**  The number of vehicles observed in lane 3 for the sample period.
  - **occupancy3 (double):** The fraction of each sample period during which the detector in lane 3 output is “1”.
  - **speed3 (double):**  The average speed of vehicles in lane 3 during the sample period.
  - **flow4 (int):**  Null for this location. The number of vehicles observed in lane 4 for the sample period.
  - **occupancy4 (double):** Null for this location. The fraction of each sample period during which the detector in lane 4 output is “1”.
  - **speed4 (double):**  Null for this location. The average speed of vehicles in lane 4 during the sample period.
  - **flow5 (int):**  Null for this location. The number of vehicles observed in lane 5 for the sample period.
  - **occupancy5 (double):** Null for this location. The fraction of each sample period during which the detector in lane 5 output is “1”.
  - **speed5 (double):**  Null for this location. The average speed of vehicles in lane 5 during the sample period.
  - **flow6 (int):**  Null for this location. The number of vehicles observed in lane 6 for the sample period.
  - **occupancy6 (double):** Null for this location. The fraction of each sample period during which the detector in lane 6 output is “1”.
  - **speed6 (double):**  Null for this location. The average speed of vehicles in lane 6 during the sample period.
  - **flow7 (int):**  Null for this location. The number of vehicles observed in lane 7 for the sample period.
  - **occupancy7 (double):** Null for this location. The fraction of each sample period during which the detector in lane 7 output is “1”.
  - **speed7 (double):**  Null for this location. The average speed of vehicles in lane 7 during the sample period.
  - **flow8 (int):**  Null for this location. The number of vehicles observed in lane 8 for the sample period.
  - **occupancy8 (double):** Null for this location. The fraction of each sample period during which the detector in lane 8 output is “1”.
  - **speed8 (double):**  Null for this location. The average speed of vehicles in lane 8 during the sample period.

# Source and License

This data was built from data sets publicly available on [Caltrans Performance Measurement System (PeMS)](https://pems.dot.ca.gov/). It is provided here for demonstrative use without any warranty as to the accuracy, reliability, or completeness of the data.
