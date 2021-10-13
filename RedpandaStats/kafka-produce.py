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

def convertUnit(inputUnit):
    if inputUnit ==  'GiB': return 1073741824
    if inputUnit ==  'MiB': return 1048576
    if inputUnit ==  'kiB': return 1024
    if inputUnit ==  'GB': return 1000000000
    if inputUnit ==  'MB': return 1000000
    if inputUnit ==  'kB': return 1000
    else: return 1

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
            "memoryUsage": int(float(re.findall('\d*\.?\d+',args[3])[0])*float(convertUnit(args[3][len(re.findall('\d*\.?\d+',args[3])[0]):]))),
            "memoryLimit": int(float(re.findall('\d*\.?\d+',args[5])[0])*float(convertUnit(args[5][len(re.findall('\d*\.?\d+',args[5])[0]):]))),
            "memoryPercent": re.findall('\d*\.?\d+',args[6])[0],
            "networkInput": int(float(re.findall('\d*\.?\d+',args[7])[0])*float(convertUnit(args[7][len(re.findall('\d*\.?\d+',args[7])[0]):]))),
            "networkOutput": int(float(re.findall('\d*\.?\d+',args[9])[0])*float(convertUnit(args[9][len(re.findall('\d*\.?\d+',args[9])[0]):]))),
            "blockInput": int(float(re.findall('\d*\.?\d+',args[10])[0])*float(convertUnit(args[10][len(re.findall('\d*\.?\d+',args[10])[0]):]))),
            "blockOutput": int(float(re.findall('\d*\.?\d+',args[12])[0])*float(convertUnit(args[12][len(re.findall('\d*\.?\d+',args[12])[0]):]))),

            "pids": re.findall('\d*\.?\d+',args[13])[0]
            }

        producer.produce(topic=topic_name, key=None, value=json.dumps(container))
        producer.flush()
        time.sleep(0.5)
