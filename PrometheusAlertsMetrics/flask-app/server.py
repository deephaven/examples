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
        session = Session(host="envoy") #"envoy" is the host within the docker application
        count = max_count
    except:
        print("Failed to connect to Deephaven... Waiting to try again")
        time.sleep(2)
        count += 1

if session is None:
    sys.exit("Failed to connect to Deephaven after 5 attempts")

#Initializes Deephaven with the table and an update method.
#The session.run_script() method is used to execute Python code in Deephaven.
init = """
from deephaven import DynamicTableWriter
from deephaven.DBTimeUtils import convertDateTime, currentTime
import deephaven.Types as dht

table_writer = DynamicTableWriter(
    ["PrometheusDateTime", "Job", "Instance", "AlertIdentifier", "Status", "AlertIngestDateTime"],
    [dht.datetime, dht.string, dht.string, dht.string, dht.string, dht.datetime]
)
prometheus_alerts = table_writer.getTable()

def update_prometheus_alerts(date_time_string, job, instance, alert_identifier, status):
    date_time = convertDateTime(date_time_string)
    table_writer.logRow(date_time, job, instance, alert_identifier, status, currentTime())
"""
session.run_script(init)

#Template to trigger the table update
update_template = """
update_prometheus_alerts("{date_time_string}", "{job}", "{instance}", "{alert_identifier}", "{status}")
"""

#Template to join the 2 dynamic tables on time stamps
join_tables_on_time_stamps = """
nanos_bin = 500000000 #We want to floor our Prometheus time stamps to half a second

prometheus_alerts_floored = prometheus_alerts.update(
    "PrometheusDateTimeFloored = lowerBin(PrometheusDateTime, nanos_bin)"
).dropColumns("PrometheusDateTime")

prometheus_metrics_floored = prometheus_metrics.update(
    "PrometheusDateTimeFloored = lowerBin(PrometheusDateTime, nanos_bin)"
).dropColumns("PrometheusDateTime")

prometheus_alerts_metrics = prometheus_alerts_floored.join(prometheus_metrics_floored, "PrometheusDateTimeFloored, Job, Instance").update(
    "Delay = format(minus(AlertIngestDateTime, MetricIngestDateTime))"
)
"""

tables_joined = False

@app.route('/', methods=['POST'])
def receive_alert():
    request_json = request.json
    date_time_string = None
    job = None
    instance = None
    alert_identifier = None
    status = None

    #For every alert, build the method call to update the alerts table
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

        #Executes the alert table update in Deephaven
        session.run_script(update_template.format(date_time_string=date_time_string, job=job, instance=instance,
                alert_identifier=alert_identifier, status=status))

    #If we haven't already joined the tables into a new table, run that script
    global tables_joined
    if not tables_joined:
        session.run_script(join_tables_on_time_stamps)
        tables_joined = True

    return "Request received"

app.run(port=5000, host="0.0.0.0")
