from deephaven import DynamicTableWriter, Types as dht
from deephaven.DateTimeUtils import convertDateTime
# Ensure fitparse is installed.
import os
try:
    from fitparse import FitFile
except ImportError:
    os.system("pip install fitparse")
    from fitparse import FitFile

# Change to the name of the downloaded file (including any intermediate directory added to docker)
fitfile = FitFile('/data/examples/Fit/ThursMorn.fit')

# See the size of your file
records = list(fitfile.get_messages('record'))
print("Number of data points: {}".format(len(records)))

# Setup deephaven tables to hold results
# Heart rate
column_names = ["Timestamp", "HeartRate"]
column_types = [dht.datetime, dht.int_]
hr_table_writer = DynamicTableWriter(column_names, column_types)
heart_rate_data = hr_table_writer.getTable()
# Gps data
column_names = ["Timestamp", "EnhancedAltitude", "EnhancedSpeed", "GPSAccuracy", "PositionLat", "PositionLong", "Speed"]
column_types = [dht.datetime, dht.double, dht.double, dht.int_, dht.int_, dht.int_, dht.double]
gps_table_writer = DynamicTableWriter(column_names, column_types)
gps_data = gps_table_writer.getTable()

# Set timezone based on preferences. Fit data may not include timezone
timezone = "MT"
timezone = " " + timezone # Ensure there is a blank space before timezone for later parsing.

# Process in smaller batches first, until you are happy with the results you are working with
counter = 20
counter = len(records) + 1

## Debug your files by looking at individual records at a time.
# record = records[0]
# for field in record:
#     print (field.name, field.value, field.units)
#
## In my example
## records[1] is an example of enhanced gps
## records[3] is an example of heart rate
## records[0] is an example of step counter (guessing)

# Get all data messages that are of type record
for record in fitfile.get_messages('record'):
    mode="None"

    if (counter > 0):
        counter -= 1
    else:
        break

    for field in record:
        if field.name.startswith('heart_rate'):
            mode="hr"
        if field.name.startswith('enhanced'):
            mode="gps"
        # Other types can be added, following a similar pattern.

    # Go through all the data entries in this record
    items=list(record)
    if (mode == "hr"):
        raw_heart_rate = str(items[0]).split()[1]
        final_heart_rate = int(raw_heart_rate)
        raw_time = str(items[1]).split()[1]
        final_time = convertDateTime(raw_time.replace(" ", "T") + timezone)
        hr_table_writer.logRow(final_time, final_heart_rate)

    if (mode == "gps"):
        raw_time = str(items[6])[11:30]
        final_time = convertDateTime(raw_time.replace(" ", "T") + timezone)

        final_altitude = float(str(items[0]).split()[1])
        final_enh_speed = float(str(items[1]).split()[1])
        final_pos_lat = int(str(items[3]).split()[1])
        final_pos_long = int(str(items[4]).split()[1])
        final_speed = float(str(items[5]).split()[1])

        raw_gps_acc = str(items[2]).split()[1]
        # If preferred, the col type for GPS could be set as String, then further processing done even when value is None
        if raw_gps_acc != "None":
            final_gps_acc = int(str(items[2]).split()[1])
            gps_table_writer.logRow(final_time, final_altitude, final_enh_speed, final_gps_acc, final_pos_lat, final_pos_long, final_speed)