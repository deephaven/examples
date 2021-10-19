# Prometheus Alerts Metrics

[Prometheus](https://prometheus.io/) is an open-source systems monitoring and alerting toolkit that collects and stores its metrics as time series data. This sample app shows how to ingest data from [Prometheus alerts](https://prometheus.io/docs/alerting/latest/configuration/#webhook_config) and [Prometheus's API](https://prometheus.io/docs/prometheus/latest/querying/api/) into a single [Deephaven](https://deephaven.io/) table.

## How it works

This app runs a [Python Flask server](https://flask.palletsprojects.com/en/2.0.x/) wherever it is deployed, and also runs a secondary script using [Deephaven's application mode](https://deephaven.io/core/docs/how-to-guides/app-mode/).

### Components

* `Dockerfile` - The dockerfile for the application. This extends the default Deephaven image to add dependencies. See our guide, [How to install Python packages](https://deephaven.io/core/docs/how-to-guides/install-python-packages/#add-packages-to-a-custom-docker-image), for more information.
* `docker-compose.yml` - The Docker Compose file for the application. This is mostly the same as the [Deephaven docker-compose file](https://raw.githubusercontent.com/deephaven/deephaven-core/main/containers/python-examples/docker-compose.yml) with modifications to run Prometheus, application mode, and the Python server.
* `prometheusDhAlertMetricsStart.sh` - A simple helper script to launch the application.
* `app.d/app.app` - The Deephaven application mode app file.
* `app.d/requirements.txt` - Python dependencies for the Deephaven application mode script.
* `app.d/prometheus.py` - The Python script that runs through Deephaven application mode which pulls the data from Prometheus and stores it into Deephaven.
* `flask-app/requirements.txt` - Python dependencies for the Python server.
* `flask-app/server.py` - The Python server that accepts the Prometheus alert webhooks.
* `flask-app/Dockerfile` - The Dockerfile for the Python server.
* `alertmanager/config.yml` - The Prometheus alerts rules. This includes the configuration for the webhook alerts destination URL.
* `prometheus/prometheus.yml` - The Prometheus config file. This has been thinned down to handle just the alerts.
* `prometheus/rules.yml` - The Prometheus alert rules file. This includes the configuration for what triggers alerts.

### High level overview

#### Python Flask server

This part of the app runs a [Python Flask server](https://flask.palletsprojects.com/en/2.0.x/) that accepts [Prometheus alert webhooks](https://prometheus.io/docs/alerting/latest/configuration/#webhook_config). The webhooks are deserialized, and the desired values are extracted and stored into a Deephaven table to show when alerts were fired and resolved.

The [`pydeephaven`](https://pypi.org/project/pydeephaven/) package is used for the server to interact with Deephaven.

#### Deephaven Application Mode script

This part of the app pulls data from [Prometheus's API](https://prometheus.io/docs/prometheus/latest/querying/api/) through HTTP requests. The API responses are deserialized, and the desired values are extracted and stored into a Deephaven table to show the metrics of our Prometheus queries over time.

### Combining tables

Once the two tables are created, they are combined using a [join operation](https://deephaven.io/core/docs/reference/table-operations/join/join/) in order to display a table that shows the values of the Prometheus queries at the time when an alert was either fired or resolved.

The metrics table contains the following columns:

`PrometheusDateTime, PrometheusQuery, Job, Instance, Value, MetricIngestDateTime`

The alerts table contains the following columns:

`PrometheusDateTime, Job, Instance, AlertIdentifier, Status, AlertIngestDateTime`

The tables are combined on the `Job`, `Instance`, and the computed `PrometheusDateTimeFloored` columns.

#### `lowerBin`

Prometheus sends a timestamp with its alert webhooks, and includes a timestamp when querying metrics data. We store this in the `PrometheusDateTime` column. This is useful for mapping our metrics to an alert, but since we are querying our metrics on a timed cadence, we can't guarantee that the alert's timestamp will match our query's timestamp. So how do we map a query metric to an alert? We can use [lowerBin](https://deephaven.io/core/docs/reference/time/datetime/lowerBin/) to "floor" our timestamps. This example floors the timestamps to the nearest half second. This works because we pull data on half second intervals, and Prometheus's alertmanager is configured to check every second before determining if an alert should be fired or resolved.

This app uses `lowerBin` to compute the `PrometheusDateTimeFloored` column.

## Dependencies

* The [Deephaven-core dependencies](https://github.com/deephaven/deephaven-core#required-dependencies) are required for this project.
* If you want to use a different Prometheus instance than the default instance, you will need to [install Prometheus](https://prometheus.io/docs/prometheus/latest/installation/) at your desired location.

## Launch

Before launching, you can modify the `PROMETHEUS_QUERIES` and `BASE_URL` values in `prometheus.py` to see the results of different queries, and to point the application at different Prometheus instances. You can also modify any of the files in the `prometheus/` or `alertmanager/` directories to configure what alerts are sent, and where the alerts are sent. The default values can be used to demonstrate functionality.

Once you are set, simply run the following to launch the app:

```
sh prometheusDhAlertMetricsStart.sh
```

Your Flask server should be running, and you can go to [http://localhost:10000/ide](http://localhost:10000/ide) to view the tables in the top right **Panels** tab! These tables will update as more query metrics are ingested, and more alerts are fired and resolved.

There will be a few tables in the panels tab. The main ones are `prometheus_alerts` (alerts fired and received), `prometheus_metrics` (Prometheus query data over time), and `prometheus_alerts_metrics` (the combined alerts and metrics data).

## Related apps

This app is built off of 2 previous existing apps, [Prometheus Alerts](https://github.com/deephaven-examples/prometheus-alerts) and [Prometheus Metrics](https://github.com/deephaven-examples/prometheus-metrics). Feel free to check them out for more Prometheus examples!
