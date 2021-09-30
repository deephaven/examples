# Prometheus

[Prometheus](https://prometheus.io/) is an open-source systems monitoring and alerting toolkit that collects and stores its metrics as time series data. This sample app shows how to ingest data from Prometheus into [Deephaven](https://deephaven.io/).

## How it works

### Deephaven application mode

This app runs using [Deephaven's application mode](https://deephaven.io/core/docs/how-to-guides/app-mode/).

### Components

* `Dockerfile` - The dockerfile for the application. This extends the default Deephaven image to add dependencies. See our guide, [How to install Python packages](https://deephaven.io/core/docs/how-to-guides/install-python-packages/#add-packages-to-a-custom-docker-image), for more information.
* `docker-compose.yml` - The Docker Compose file for the application. This is mostly the same as the [Deephaven docker-compose file](https://raw.githubusercontent.com/deephaven/deephaven-core/main/containers/python-examples/docker-compose.yml) with modifications to run Prometheus, application mode, and the custom dependencies.
* `app.app` - The Deephaven application mode app file.
* `requirements.txt` - Python dependencies for the application.
* `start.sh` - A simple helper script to launch the application.
* `prometheus.py` - The Python script that pulls the data from Prometheus and stores it into Deephaven.

### High level overview

This app pulls data from [Prometheus's API](https://prometheus.io/docs/prometheus/latest/querying/api/) through HTTP requests. The API responses are deserialized, and the desired values are extracted and stored into a Deephaven table.

Once data is collected and tables are created, various [Deephaven queries](https://deephaven.io/core/docs/how-to-guides/simple-python-query/) are then performed on the tables.

This app writes to Deephaven tables both statically and dynamically.

## Dependencies

* The [Deephaven-core dependencies](https://github.com/deephaven/deephaven-core#required-dependencies) are required for this project.
* If you want to use a different Prometheus instance than the default instance, you will need to [install Prometheus](https://prometheus.io/docs/prometheus/latest/installation/) at your desired location.

## Launch

Before launching, you can modify the `PROMETHEUS_QUERIES` and `BASE_URL` values in `prometheus.py` to see the results of different queries, and to point the application at different Prometheus instances.

Once you are set, simply run the following to launch the app:

```
sh start.sh
```

Go to [http://localhost:10000/ide](http://localhost:10000/ide) to view the tables in the top right **Panels** tab!

### Ngrok


:::note

If you are running Prometheus locally and seeing errors like:

```
HTTPConnectionPool(host='localhost', port=9090): Max retries exceeded with url: /api/v1/query?query=up (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f4619929a90>: Failed to establish a new connection: [Errno 111] Connection refused'))
```

you may need to use [Ngrok](https://ngrok.com/) to make HTTP requests to your Prometheus instance. 

:::

After [installing Ngrok](https://ngrok.com/download), run the following in a separate terminal:

```
ngrok http 9090
```

Use the URL on the terminal that forwards to <http://localhost:9090> to construct the `BASE_URL` value. Edit this value in `prometheus.py` and re-launch the application. For example:

```
BASE_URL = "{base}/api/v1/query".format(base="http://c818-2603-6081-2300-2640-50c5-4e0a-6c65-498d.ngrok.io")
```
