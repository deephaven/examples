# Taxi Sample data

This folder contains sample data files concerning taxi rides in NYC from October 31, 2018 and November 1, 2018 that work within the Deephaven console.

## Table of contents

- `taxi.parquet`: uncompressed parquet data format
- `taxi.csv`: csv data format

## Fields

  - **int64** VendorID
  - **int64**  tpep_pickup_datetime (TIMESTAMP(MICROS,false))
  - **int64**  tpep_dropoff_datetime (TIMESTAMP(MICROS,false))
  - **int64**  passenger_count
  - **double**  trip_distance
  - **int64**  RatecodeID
  - **binary**  store_and_fwd_flag (STRING)
  - **int64**  PULocationID
  - **int64**  DOLocationID
  - **int64**  payment_type
  - **double**  fare_amount
  - **double**  extra
  - **double**  mta_tax
  - **double**  tip_amount
  - **double**  tolls_amount
  - **double**  improvement_surcharge
  - **double**  total_amount

# Source and License

This data was built from data sets publicly available on [Microsoft Azure](https://azure.microsoft.com/en-us/services/open-datasets/catalog/nyc-taxi-limousine-commission-yellow-taxi-trip-records/). It is provided here for demonstrative use without any warranty as to the accuracy, reliability, or completeness of the data.
