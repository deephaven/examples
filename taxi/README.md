# Taxi Sample data

This folder contains sample data files concerning taxi rides in NYC from October 31, 2018 and November 1, 2018 that work within the Deephaven console.

## Table of contents

- `taxi.parquet`: uncompressed parquet data format
- `taxi.csv`: csv data format

## Fields

  - **VendorID (int64):**  A code indicating the TPEP provider that provided the record. 1 = Creative Mobile Technologies, LLC; 2 = VeriFone Inc.
  - **tpep_pickup_datetime (int64):**  The date and time when the meter was engaged.
  - **tpep_dropoff_datetime (int64):**  The date and time when the meter was disengaged.
  - **passenger_count (int64):**  The number of passengers in the vehicle. This is a driver-entered value.
  - **trip_distance (double):**  The elapsed trip distance in miles reported by the taximeter.
  - **RatecodeID (int64):**  The final rate code in effect at the end of the trip. 1 = Standard rate; 2 = JFK; 3 = Newark; 4 = Nassau or Westchester; 5 = Negotiated fare; 6 = Group ride.
  - **store_and_fwd_flag (binary STRING):**  This flag indicates whether the trip record was held in vehicle memory before sending to the vendor, aka “store and forward,” because the vehicle did not have a connection to the server. Y = store and forward trip; N = not a store and forward trip.
  - **PULocationID (int64):**  TLC Taxi Zone in which the taximeter was engaged.
  - **DOLocationID (int64):**  TLC Taxi Zone in which the taximeter was disengaged.
  - **payment_type (int64):**  A numeric code signifying how the passenger paid for the trip. 1 = Credit card; 2 = Cash; 3 = No charge; 4 = Dispute; 5 = Unknown; 6 = Voided trip
  - **fare_amount (double):**  The time-and-distance fare calculated by the meter.
  - **extra (double):**  Miscellaneous extras and surcharges. Currently, this only includes the $0.50 and $1 rush hour and overnight charges.
  - **mta_tax (double):**  $0.50 MTA tax that is automatically triggered based on the metered rate in use.
  - **tip_amount (double):**  This field is automatically populated for credit card tips. Cash tips are not included.
  - **tolls_amount (double):**  Total amount of all tolls paid in trip.
  - **improvement_surcharge (double):**  $0.30 improvement surcharge assessed trips at the flag drop. The improvement surcharge began being levied in 2015.
  - **total_amount (double):**  The total amount charged to passengers. Does not include cash tips.

# Source and License

This data was built from data sets publicly available on [Microsoft Azure](https://azure.microsoft.com/en-us/services/open-datasets/catalog/nyc-taxi-limousine-commission-yellow-taxi-trip-records/). It is provided here for demonstrative use without any warranty as to the accuracy, reliability, or completeness of the data.
