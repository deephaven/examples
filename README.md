
# Sample Data Sets

This directory contains several sample data sets:

* **gsod:** Global Surface Summary of the Day (GSOD) weather data
* **iris:** Iris species classification data
* **metriccentury:** position and performance information of a cyclist during a long bicycle ride

## Installation Instructions
1. Clone the repo `https://github.com/deephaven/deephaven-core`
2. From the root of your `deephaven-core` clone, run:
   1. `docker build -t deephaven/examples samples`
   2. `docker run --rm -v "$(pwd)/docker/core/data:/data" deephaven/examples download`

## After Installation

The commands above populate `docker/core/data/examples` in the `deephaven-core` clone with the three sample data sets.
