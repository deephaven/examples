from deephaven import DynamicTableWriter, Types as dht
from deephaven.DBTimeUtils import convertDateTime
from fitparse import FitFile

# Change to the name of the downloaded file (including any intermediate directory added to docker)
fitfile = FitFile('/data/ThursMorn.fit')

# See the size of your file
records = list(fitfile.get_messages('record'))
print("Number of data points:" + str(len(records)))

# Setup deephaven tables to hold results
# Heart rate
columnNames = ["Timestamp", "Heart Rate"]
columnTypes = [dht.datetime, dht.int_]
hrTableWriter = DynamicTableWriter(columnNames, columnTypes)
heartRateData = hrTableWriter.getTable()
# Gps data
columnNames = ["Timestamp", "Enhanced Altitude m", "Enhanced Speed m/s", "GPPS Accuracy m", "Position lat semicircles", "Position long semicircles", "Speed m/s"]
columnTypes = [dht.datetime, dht.double, dht.double, dht.int_, dht.int_, dht.int_, dht.double]
gpsTableWriter = DynamicTableWriter(columnNames, columnTypes)
gpsData = gpsTableWriter.getTable()

# Set timezone based on preferences. Fit data may not include timezone
timezone="MT"
timezone=" " + timezone # Ensure there is a blank space before timezone for later parsing.

# Process in smaller batches first, until you are happy with the results you are working with
counter = 20
counter = len(records)+1

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
    if (mode == "hr" ):
        rawHeartRate=str(items[0]).split(" ")[1]
        finalHeartRate=int(rawHeartRate)
        rawTime=str(items[1]).split(" ")[1]
        finalTime=convertDateTime(rawTime.replace(" ", "T") + timezone)
        hrTableWriter.logRow(finalTime, finalHeartRate)

    if (mode == "gps" ):
        rawTime=str(items[6])[11:30]
        finalTime=convertDateTime(rawTime.replace(" ", "T") + timezone)

        finalAltitude=float(str(items[0]).split(" ")[1])
        finalEnhSpeed=float(str(items[1]).split(" ")[1])
        finalPosLat=int(str(items[3]).split(" ")[1])
        finalPosLong=int(str(items[4]).split(" ")[1])
        finalSpeed=float(str(items[5]).split(" ")[1])

        rawGPSAcc=str(items[2]).split(" ")[1]
        # If preferred, the col type for GPS could be set as String, then further processing done even when value is None
        if rawGPSAcc != "None":
            finalGPSAcc=int(str(items[2]).split(" ")[1])
            gpsTableWriter.logRow(finalTime, finalAltitude,finalEnhSpeed,finalGPSAcc,finalPosLat,finalPosLong,finalSpeed)
