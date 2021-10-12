# Example scrupt to produce kafka messages to Deephaven from docker stats using RedPanda.
#
# To run this script, you need confluent-kafka libraries installed.
# To create a dedicated venv for it, you can do:
#
# $ mkdir confluent-kafka; cd confluent-kafka
# $ python3 -m venv confluent-kafka
# $ cd confluent-kafka
# $ source bin/activate
# $ pip3 install confluent-kafka
#
# Note: On a Mac you may need to install the librdkafka package.
# You can use "brew install librdkafka" if the pip3 command fails
# with an error like "librdkafka/rdkafka.h' file not found"
# as found at confluentinc/confluent-kafka-python#166.
#
# Examples of use for DH testing together with web UI.
#
# == Common to all:
#
#  * Start the redpanda compose: (cd RedpandaStats && docker-compose up --build)
#
# == Example
#
# From [http://localhost:10000/ide](http://localhost:10000/ide/):
# from deephaven import KafkaTools as kt
# from deephaven import Types as dht
# result= kt.consumeToTable({'bootstrap.servers': 'redpanda:29092'} , 'docker-stats', key=kt.IGNORE, value=kt.json([
#    ('container', dht.string),
#    ('name',   dht.string),
#    ('cpu',  dht.string),
#    ('memory usage',   dht.string),
#    ('memory limit', dht.string),
#    ('memory %',   dht.string),
#    ('network i',  dht.string),
#    ('network o',    dht.string),
#    ('block i',  dht.string),
#    ('block o',    dht.string),
#    ('pids',    dht.string)
#    ]),table_type = 'append')
#
# Run this script on the host (not on a docker image):
# $ python3 ./kafka-produce.py


from confluent_kafka import Producer

import sys
import json
import time
import struct
import subprocess

topic_name = 'docker-stats'

while True:
    data = subprocess.check_output("docker stats --no-stream", shell=True).decode('utf8')

    container = {}

    def delivery_report(err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message key=|{}|, value=|{}| delivered to topic {} partition {}'
                  .format(msg.key(), msg.value(), msg.topic(), msg.partition()))

    lines = data.splitlines()
    for line in lines[1:]:
        args = line.split( )
        if len(args) == 14:
            container = {
            "container": args[0],
            "name": args[1],
            "cpu": args[2],
            "memory usage": args[3],
            "memory limit": args[5],
            "memory %": args[6],
            "network i": args[7],
            "network o": args[9],
            "block i": args[10],
            "block o": args[12],
            "pids": args[13]
            }

        # convert into JSON:
        y = json.dumps(container)


        producer = Producer({
            'bootstrap.servers': 'localhost:9092',
            'on_delivery': delivery_report,
        })


        producer.produce(topic=topic_name, key=None, value=y)
        producer.flush()
        time.sleep(0.5)



def dump():
    ps_keys = ["container", "image", "command", "created", "status", "ports", "names", "size"]
    stats_keys = ["container", "name", "cpu", "memory usage", "memory limit", "memory %", "network i", "slash1",
    "network o", "block i", "slash1", "block o", "pids"]
