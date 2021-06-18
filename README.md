# Example Data Sets

This repository contains open source data sets.  They are intended to be used as part of an introduction to the Deephaven Community Core Engine.  For more information, check out [Deephaven Community Core](https://github.com/deephaven/deephaven-core).

## Table of Contents

The following folders can be found in this repository:

- **[`gsod`](https://catalog.data.gov/dataset/global-surface-summary-of-the-day-gsod)** - Global Surface Summary of the Day (GSOD) weather data
- **[`iris`](https://archive.ics.uci.edu/ml/datasets/iris)** - The iris flower data set from Ronald Fisher's 1936 paper
- **[`metriccentury`](https://github.com/mikeblas/samples-junk/tree/main/metriccentury)** - Data recorded from a 100 km bike ride
- **[`DeNiro`](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html)** - Data on Robert De Niro's movies up to 2016

## Description

Each folder in this repository except parquet has two items within:

 - `README` - An explanation of everything about the data
 - `csv` - A folder with all relevant data in either CSV or TSV format

## Installation Instructions

1. Follow the README instructions on [Deephaven Community Core](https://github.com/deephaven/deephaven-core) for installing the OSS client and all required dependencies.
2. From the root of your `deephaven-core` clone, run:
   1. `docker build -t deephaven/examples samples`
   2. `docker run --rm -v "$(pwd)/docker/core/data:/data" deephaven/examples download`

The commands above mount `docker/core/data/examples` in the `deephaven-core` clone as `/data/examples` within the docker container.
