# Prometheus Alerts

[Prometheus](https://prometheus.io/) is an open-source systems monitoring and alerting toolkit that collects and stores its metrics as time series data. This sample app shows how to ingest data from [Prometheus alerts](https://prometheus.io/docs/alerting/latest/configuration/#webhook_config) via webhooks into [Deephaven](https://deephaven.io/).

## How it works

This app runs a [Python Flask server](https://flask.palletsprojects.com/en/2.0.x/) wherever it is deployed.

### Components

* `alertmanager/config.yml` - The Prometheus alerts rules. This includes the configuration for the webhook alerts destination URL.
* `docker-compose.yml` - Docker compose file that defines the Deephaven, Prometheus, and Python docker images.
* `flask-app/requirements.txt` - Python dependencies for the application.
* `flask-app/server.py` - The python server that accepts the Prometheus alert webhooks.
* `flask-app/Dockerfile` - The Dockerfile for the python server.
* `prometheus/prometheus.yml` - The Prometheus config file. This has been thinned down to handle just the alerts.
* `prometheus/rules.yml` - The Prometheus alert rules file. This includes the configuration for what triggers alerts.
* `start.sh` - Helper script that launches the application.

### High level overview

This app runs a [Python Flask server](https://flask.palletsprojects.com/en/2.0.x/) that accepts [Prometheus alert webhooks](https://prometheus.io/docs/alerting/latest/configuration/#webhook_config). The webhooks are deserialized, and the desired values are extracted and stored into a Deephaven table.

The [`pydeephaven`](https://pypi.org/project/pydeephaven/) package is used for the server to interact with Deephaven.

## Dependencies

* The [Deephaven-core dependencies](https://github.com/deephaven/deephaven-core#required-dependencies) are required for this project.

## Launch

Before launching, you can modify any of the files in the `prometheus/` or `alertmanager/` directories to configure what alerts are sent, and where the alerts are sent. The default values can be used to demonstrate functionality.

Once you are set, simply run the following to launch the app:

```
sh start.sh
```

Your Flask server should be running, and you can go to [http://localhost:10000/ide](http://localhost:10000/ide) to view the table in the top right **Panels** tab! This table will update as alerts are fired and resolved.
