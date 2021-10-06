# Example Data Sets

This repository contains open source data sets.  They are intended to be used as part of an introduction to the Deephaven Community Core Engine.  For more information, check out [Deephaven Community Core](https://github.com/deephaven/deephaven-core).

![Build CI](https://github.com/deephaven/examples/actions/workflows/build-ci.yml/badge.svg?branch=main)

## Table of Contents

The following folders can be found in this repository:

- **[`CryptoCurrency`](./CryptoCurrency)** - Script to pull live and historical data for specified cryptocurencies.
- **[`CryptoCurrencyHistory`](./CryptoCurrencyHistory)** - Data from [CoinGecko](https://www.coingecko.com/) to highlight use of CSV and Parquet data formats.
- **[`DeNiro`](./DeNiro)** - Data on Robert De Niro's movies up to 2016.
- **[`Fit`](./Fit)** - Workout results in the proprietary fit format developed by Garmin. Downloadable from Strava.
- **[`GSOD`](./GSOD)** - Global Surface Summary of the Day (GSOD) weather data.
- **[`Iris`](./Iris)** - The iris flower data set from Ronald Fisher's 1936 paper.
- **[`MetricCentury`](./MetricCentury)** - Data recorded from a 100 km bike ride.
- **[`Pems`](./Pems)** - Traffic flow data collected near Davis, CA.
- **[`Prometheus`](./Prometheus)** - System monitoring data from Prometheus.
- **[`Taxi`](./Taxi)** - Yellow Taxi trip records.
- **[`TensorFlow`](./TensorFlow)** - Statistically calculate positive/negative sentiment using machine-learning
  training mechanisms based on an RSS feed from Seeking Alpha.
- **[`TickingHeartRate`](./TickingHeartRate)** - Simulated ticking heart rate data.

## Description

Each folder in this repository has the following structure within:

 - `README` - An explanation of everything about the data
 - `csv` - A folder with all relevant data in either CSV or TSV format (if available)
 - `parquet` - A folder with all relevant data in parquet format (if available)
 - Files to run a Python and/or Groovy script will be included (if available)

## Installation Instructions

The examples script image can be pulled via:

```
docker pull ghcr.io/deephaven/examples
```

To download the examples, from the root of your `deephaven-core` clone, run:

```
docker run --rm -v "$(pwd)/data:/data" ghcr.io/deephaven/examples download
```

- The `docker run` command downloads the example data by running the examples management container.  
- The `-v "$(pwd)/data:/data"` argument mounts your local `$(pwd)/data` path as `/data` in the container.  
- The example data is stored to `/data/examples` inside the container, which is `$(pwd)/data/examples` on the local filesystem.

You can run `docker run` again to manage the example data - for example, to download a new version. To see what options are available, run:

```
docker run --rm -v "$(pwd)/data:/data" ghcr.io/deephaven/examples
```

## Build Instructions

From the root of `examples`, run:

```
docker build -t ghcr.io/deephaven/examples docker
```

The `docker build` command builds a Docker container containing a script that helps manage the examples.
That script will automate the management of the example files.  It allows you to download and update the example files without directly working with the git project hosting the examples.  This `docker build` command is only needed once; after it runs, the container is available to use on your host.
