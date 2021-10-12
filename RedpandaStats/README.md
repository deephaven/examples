# RedPanda and Deephaven

[RedPanda](https://vectorized.io/) is an open-source Kafka compatible event streaming platform. This sample app shows how to ingest Docker stats data from RedPanda into [Deephaven](https://deephaven.io/).

## How it works

### Deephaven

This app runs using [Deephaven](https://deephaven.io/core/docs/tutorials/quickstart/).

### Components

* `docker-compose.yml` - The Docker Compose file for the application. This is the same as the [Deephaven docker-compose file with RedPanda](https://deephaven.io/core/docs/how-to-guides/kafka-simple/)
* `kafka-produce.py` - The Python script that pulls the data from docker stats into streaming kafka data onto RedPanda.

### High level overview

This app pulls data from the local [docker](https://docs.docker.com/engine/reference/commandline/stats/) containers.
The data is placed into a RedPanda Kafka Stream.

Once data is collected in Kafka, [Deephaven consumes](https://deephaven.io/core/docs/how-to-guides/simple-python-query/) the stream.
