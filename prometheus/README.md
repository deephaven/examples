# Prometheus

This sample app shows how to ingest data from [Prometheus](https://prometheus.io/) into [Deephaven](https://deephaven.io/).

## How it works

### Deephaven application mode

This app runs using [Deephaven's application mode](https://deephaven.io/core/docs/how-to-guides/app-mode/).

### Components

* `Dockerfile` - The dockerfile for the application. This extends the default Deephaven image to [add dependencies](https://deephaven.io/core/docs/how-to-guides/install-python-packages/#add-packages-to-a-custom-docker-image).
* `docker-compose.yml` - The docker compose file for the application. This is mostly the same as the [Deephaven docker-compose file](https://raw.githubusercontent.com/deephaven/deephaven-core/main/containers/python-examples/docker-compose.yml) with modifications to run Prometheus, application mode, and the custom dependencies.
* `app.app` - The Deephaven application mode app file.
* `requirements.txt` - Python dependencies for the application.
* `start.sh` - A simple helper script to launch the application.
* `prometheus.py` - The python script that pulls the data from Prometheus and stores it into Deephaven.

### High level overview

This app pulls data from [Prometheus's API](https://prometheus.io/docs/prometheus/latest/querying/api/) through HTTP requests. The API responses are deserialized, and the values are extracted and stored into a Deephaven table.

This app writes to Deephaven tables both [statically](https://deephaven.io/core/docs/how-to-guides/new-table/) and [dynamically](https://deephaven.io/core/docs/how-to-guides/dynamic-table-writer/).

## Dependencies

* The [Deephaven-core dependencies](https://github.com/deephaven/deephaven-core#required-dependencies) are required for this project.
* If you want to use a different Prometheus instance than the default instance, you will need to [install Prometheus](https://prometheus.io/docs/prometheus/latest/installation/) at your desired location.

## Launch

Before launching, you can modify the `PROMETHEUS_QUERIES` and `BASE_URL` values in `prometheus.py` to see the results of different queries, and to point the application at different Prometheus instances.

Once you are set, simply run

```
sh start.sh
```

to launch the app. You can go to http://localhost:10000/ide to view the tables in the top right `Panels` tab!
