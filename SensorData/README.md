# Sensor Dataset

This folder contains two subfolders: `csv` and `parquet`. Each holds the same dataset in CSV and Apache Parquet format, respectively.

## The Dataset

The sensor data contained in this folder is a modified version of [this dataset](https://www.kaggle.com/datasets/halimedogan/wireless-sensor-network-data) found on Kaggle. It contains 2.3 millions rows, and the following columns:

- `Timestamp` - A Deephaven DateTime column.
  - The original dataset's timestamps are given in string format and are spaced by seconds to minutes for each measurement. This dataset's modified timestamps are much closer together, the the two original columns have been combined into one.
- `sensor_id` - Each sensor's unique ID number.
- `sensor_type` - The sensor type given by a char. All sensors are of type `B`.
  - The original dataset contains one measurement of type `b`. 
- `temp_C` - The temperature in Celsius for each measurement.
- `hpa_div_4` - The pressure in hectopascals (hPa) divided by four for each measurement. For reference, one atmosphere is 1013.25 hectopascals.
- `batterylevel` - The battery level of each sensor.
- `sensor_cycle` - The sensor cycle number.

## Source and license

This data was obtained from [Kaggle](https://www.kaggle.com/). The original link, authored by [Halime Doğan](https://www.kaggle.com/halimedogan), can be found [here](https://www.kaggle.com/datasets/halimedogan/wireless-sensor-network-data). It is provided for demonstrative use without any warranty as to the accuracy, reliability, or completeness of the data.
