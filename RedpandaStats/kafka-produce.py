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

def convert_unit(input_Unit):
    if input_Unit ==  'GiB': return 1073741824
    if input_Unit ==  'MiB': return 1048576
    if input_Unit ==  'kiB': return 1024
    if input_Unit ==  'GB': return 1000000000
    if input_Unit ==  'MB': return 1000000
    if input_Unit ==  'kB': return 1000
    else: return 1


def get_raw(value_with_unit_str):
  value_str = re.findall('\d*\.?\d+',value_with_unit_str)[0]
  unit_str = value_with_unit_str[len(value_str):]
  return int(float(value_str) * float(convert_unit(unit_str)))


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
            "memoryUsage": get_raw(args[3]),
            "memoryLimit": get_raw(args[5]),
            "memoryPercent": re.findall('\d*\.?\d+',args[6])[0],
            "networkInput": get_raw(args[7]),
            "networkOutput": get_raw(args[9]),
            "blockInput": get_raw(args[10]),
            "blockOutput": get_raw(args[12]),
            "pids": re.findall('\d*\.?\d+',args[13])[0]
            }

        producer.produce(topic=topic_name, key=None, value=json.dumps(container))
        producer.flush()
        time.sleep(0.5)
