# RedPanda and Deephaven

[RedPanda](https://vectorized.io/) is an open-source Kafka compatible event streaming platform. This sample app shows how to ingest Docker stats data from RedPanda into [Deephaven](https://deephaven.io/).

## How it works

### Deephaven

This app runs using [Deephaven](https://deephaven.io/core/docs/tutorials/quickstart/) with Docker.

### Components

* `docker-compose.yml` - The Docker Compose file for the application. This is the same as the [Deephaven docker-compose file with RedPanda](https://deephaven.io/core/docs/how-to-guides/kafka-simple/)
* `kafka-produce.py` - The Python script that pulls the data from docker stats into streaming kafka data onto RedPanda.

### High level overview

This app pulls data from the local [docker](https://docs.docker.com/engine/reference/commandline/stats/) containers.
The data is placed into a RedPanda Kafka Stream.

Once data is collected in Kafka, [Deephaven consumes](https://deephaven.io/core/docs/how-to-guides/simple-python-query/) the stream.



### To run script


In your 'RedpandaStats' directory, bring up this version of the deployment:

```bash
docker-compose up -d
```

This starts the containers needed for RedPanda and Deephaven.

To start listening to the Kafka topic `docker-stats`, navigate to [http://localhost:10000/ide](http://localhost:10000/ide/) and enter:

```python
from deephaven import KafkaTools as kt
from deephaven import Types as dht

result= kt.consumeToTable({'bootstrap.servers': 'redpanda:29092'} , 'docker-stats', key=kt.IGNORE, value=kt.json([
    ('container', dht.string),
    ('name',   dht.string),
    ('cpuPercent',  dht.double),
    ('memoryUsage',   dht.string),
    ('memoryLimit', dht.string),
    ('memoryPercent',   dht.double),
    ('networkInput',  dht.string),
    ('networkOutput',    dht.string),
    ('blockInput',  dht.string),
    ('blockOutput',    dht.string),
    ('pids',    dht.int32)
    ]),table_type = 'append')
  ```

  To produce the Kafka stream, execute the `kafka-produce.py` script in your terminal:

  ```bash
  python3 ./kafka-produce.py
  ```
