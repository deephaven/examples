# Redpanda and Deephaven

[Redpanda](https://vectorized.io/) is an open-source Kafka-compatible event streaming platform. This sample app shows how to ingest Docker stats data from Redpanda into [Deephaven](https://deephaven.io/).


## How it works

### Deephaven

This app runs using Deephaven with Docker. See our [Quickstart](https://deephaven.io/core/docs/tutorials/quickstart/).

### Components

* `docker-compose.yml` - The Docker Compose file for the application. This is the same as the Deephaven `docker-compose` file with Redpanda described in our [Simple Kafka import](https://deephaven.io/core/docs/how-to-guides/kafka-simple/).
* `kafka-produce.py` - The Python script that pulls the data from Docker stats into streaming Kafka data onto Redpanda.

### High level overview

This app pulls data from the local [Docker](https://docs.docker.com/engine/reference/commandline/stats/) containers.
The data is placed into a Redpanda Kafka stream.

Once data is collected in Kafka, Deephaven consumes the stream.

### To run script

In your 'RedpandaStats' directory, bring up this version of the deployment:

```bash
docker-compose up -d
```

This starts the containers needed for Redpanda and Deephaven.

To start listening to the Kafka topic `docker-stats`, navigate to [http://localhost:10000/ide](http://localhost:10000/ide/) and enter:


```python
from deephaven import KafkaTools as kt
from deephaven import Types as dht

result= kt.consumeToTable({'bootstrap.servers': 'redpanda:29092'} , 'docker-stats', key=kt.IGNORE, value=kt.json([
    ('container', dht.string),
    ('name',   dht.string),
    ('cpuPercent',  dht.double),
    ('memoryUsage',   dht.int64),
    ('memoryLimit', dht.int64),
    ('memoryPercent',   dht.double),
    ('networkInput',  dht.int64),
    ('networkOutput',    dht.int64),
    ('blockInput',  dht.int64),
    ('blockOutput',    dht.int64),
    ('pids',    dht.int32)
    ]),table_type = 'append')
  ```

To produce the Kafka stream, execute the `kafka-produce.py` script in your terminal:

  ```bash
  python3 ./kafka-produce.py
  ```
