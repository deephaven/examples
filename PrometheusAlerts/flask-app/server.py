from flask import Flask, request
from pydeephaven import Session

import time
import sys

app = Flask(__name__)
session = None

#Simple retry loop in case the server tries to launch before Deephaven is ready
count = 0
max_count = 5
while (count < max_count):
    try:
        session = Session()
        count = max_count
    except:
        print("Failed to connect to Deephaven... Waiting to try again")
        time.sleep(2)
        count += 1

if session is None:
    sys.exit("Failed to connect to Deephaven after 5 attempts")

#Initializes the Deephaven server with the table and an update method
init = """
from deephaven import DynamicTableWriter
from deephaven.DBTimeUtils import convertDateTime
import deephaven.Types as dht

table_writer = DynamicTableWriter(
    ["DateTime", "Job", "Instance", "AlertIdentifier", "Status"],
    [dht.datetime, dht.string, dht.string, dht.string, dht.string]
)
alerts_table = table_writer.getTable()

def update_alerts_table(date_time_string, job, instance, alert_identifier, status):
    date_time = convertDateTime(date_time_string)    
    table_writer.logRow(date_time, job, instance, alert_identifier, status)
"""

#Triggers the table update
update_template = """
update_alerts_table("{date_time_string}", "{job}", "{instance}", "{alert_identifier}", "{status}")
"""

session.run_script(init)

@app.route('/', methods=['POST'])
def receive_alert():
    request_json = request.json
    print(request_json)
    date_time_string = None
    job = None
    instance = None
    alert_identifier = None
    status = None

    for alert in request_json["alerts"]:
        status = alert["status"]
        #Dates come in the format yyyy-mm-ddThh:mm:ss.sssZ, we need to
        #convert to yyyy-mm-ddThh:mm:ss.sss TZ for Deephaven
        if status == "firing":
            date_time_string = alert["startsAt"][0:-1] + " UTC"
        elif status == "resolved":
            date_time_string = alert["endsAt"][0:-1] + " UTC"
        job = alert["labels"]["job"]
        instance = alert["labels"]["instance"]
        alert_identifier = alert["labels"]["alertname"]

        session.run_script(update_template.format(date_time_string=date_time_string, job=job, instance=instance,
                alert_identifier=alert_identifier, status=status))
    return "Request received"

app.run(port=5000, host="0.0.0.0")
