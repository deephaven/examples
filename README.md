# Example Data Sets

This repository contains open source data sets.  They are intended to be used as part of an introduction to the Deephaven Community Core Engine.  For more information, check out [Deephaven Community Core](https://github.com/deephaven/deephaven-core).

![Build CI](https://github.com/deephaven/examples/actions/workflows/build-ci.yml/badge.svg?branch=main)

## Table of Contents

The following folders can be found in this repository:

- **[`gsod`](https://catalog.data.gov/dataset/global-surface-summary-of-the-day-gsod)** - Global Surface Summary of the Day (GSOD) weather data
- **[`iris`](https://archive.ics.uci.edu/ml/datasets/iris)** - The iris flower data set from Ronald Fisher's 1936 paper
- **[`metriccentury`](https://github.com/mikeblas/samples-junk/tree/main/metriccentury)** - Data recorded from a 100 km bike ride
- **[`DeNiro`](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html)** - Data on Robert De Niro's movies up to 2016
- **[`Taxi`](https://azure.microsoft.com/en-us/services/open-datasets/catalog/nyc-taxi-limousine-commission-yellow-taxi-trip-records/)** - Yellow taxi trip records

## Description

Each folder in this repository has the following structure within:

 - `README` - An explanation of everything about the data
 - `csv` - A folder with all relevant data in either CSV or TSV format (if available)
 - `parquet` - A folder with all relevant data in parquet format (if available)

## Installation Instructions

The examples script image can be pulled via: `docker pull ghcr.io/deephaven/examples`.

To download the examples, from the root of your `deephaven-core` clone, run:
    `docker run --rm -v "$(pwd)/docker/core/data:/data" ghcr.io/deephaven/examples download`

The `docker run` command downloads the example data by running the new examples management container.  The `-v "$(pwd)/docker/core/data:/data"` argument mounts your local `deephaven-core/docker/core/data` path as `/data` in the container.  The example data is stored to `/data/examples` inside the container, which is `deephaven-core/docker/core/data/examples` on the local filesystem.

You can run `docker run` again to manage the example data -- for example, to download a new version. To see what options are available, run:

	`docker run --rm -v "$(pwd)/docker/core/data:/data" ghcr.io/deephaven/examples`

## Build Instructions

From the root of examples, run: `docker build -t ghcr.io/deephaven/examples docker`.

The `docker build` command builds a Docker container containing a script that helps manage the examples.
That script will automate the management of the example files.  It allows you to download and update the example files without directly working with the git project hosting the examples.  This `docker build` command is only needed once; after it runs, the container is available to use on your host.
