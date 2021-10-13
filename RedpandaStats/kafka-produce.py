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
# Run this script on the host (not on a docker image):
# $ python3 ./kafka-produce.py


from confluent_kafka import Producer

import re
import json
import time
import subprocess

topic_name = 'docker-stats'

producer = Producer({
    'bootstrap.servers': 'localhost:9092',
})

while True:
    data = subprocess.check_output("docker stats --no-stream", shell=True).decode('utf8')

    container = {}

    lines = data.splitlines()
    for line in lines[1:]:
        args = line.split( )
        if len(args) == 14:
            container = {
            "container": args[0],
            "name": args[1],
            "cpuPercent": re.findall('\d*\.?\d+',args[2])[0],
            "memoryUsage": args[3],
            "memoryLimit": args[5],
            "memoryPercent": re.findall('\d*\.?\d+',args[6])[0],
            "networkInput": args[7],
            "networkOutput": args[9],
            "blockInput": args[10],
            "blockOutput": args[12],
            "pids": re.findall('\d*\.?\d+',args[13])[0]
            }

        producer.produce(topic=topic_name, key=None, value=json.dumps(container))
        producer.flush()
        time.sleep(0.5)
