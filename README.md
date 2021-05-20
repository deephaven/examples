# Example Data Sets

This repository contains three open source data sets.  They are intended to be used as part of an introduction to the Deephaven Community Core Engine.  For more information on that, check out [Deephaven Community Core](https://github.com/deephaven/deephaven-core).

## Table of Contents

The following folders can be found in this repository:

- **[`gsod`](https://catalog.data.gov/dataset/global-surface-summary-of-the-day-gsod)** - Global Surface Summary of the Day (GSOD) weather data
- **[`iris`](https://archive.ics.uci.edu/ml/datasets/iris)** - The iris flower data set from Ronald Fisher's 1936 paper
- **[`metriccentury`](https://github.com/mikeblas/samples-junk/tree/main/metriccentury)** - Data recorded from a 100 km bike ride

## Description

Each folder in this repository has two items within:

 - `README` - An explanation of everything about the data
 - `csv` - A folder with all relevant CSV files

All data in this repository is stored in standard CSV format.  The directory structure is as mentioned above.  The `gsod` folder contains 20 CSV files, while the `iris` and `metriccentury` each only contain 1.  For more information, refer to the `README` in each folder.

## Installation Instructions
1. Clone the deephaven-core repository `https://github.com/deephaven/deephaven-core`
2. From the root of your `deephaven-core` clone, run:
   1. `docker build -t deephaven/examples samples`
   2. `docker run --rm -v "$(pwd)/docker/core/data:/data" deephaven/examples download`

## After Installation

The commands above populate `docker/core/data/examples` in the `deephaven-core` clone with all of the data.
