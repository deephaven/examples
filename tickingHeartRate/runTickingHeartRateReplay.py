from deephaven.TableTools import readHeaderlessCsv
from deephaven import DynamicTableWriter, Types as dht
from deephaven import DBTimeUtils
import pathlib
import time
import threading

# Max number of csv files to pull in
csvFiles=500

# Setup deephaven tables to hold results
# Heart rate
columnNames = ["Timestamp", "Heart Rate"]
columnTypes = [dht.datetime, dht.int_]
#columnTypes = [dht.string, dht.string]
hrTableWriter = DynamicTableWriter(columnNames, columnTypes)
heartRateData = hrTableWriter.getTable()

# Function to log data to the dynamic table
def thread_func():
    for x in range(1,csvFiles):
        nextFile=("/data/csv/%d.csv" % x)
        print(nextFile)
        path = pathlib.Path(nextFile)
        if path.exists() and path.is_file():
            nextHR=readHeaderlessCsv(nextFile).update("Timestamp=Column1", "Heart_rate=Column2").select("Timestamp", "Heart_rate")
            nextRecord=nextHR.getRecord(0, "Timestamp", "Heart_rate")
            timestamp=DBTimeUtils.autoEpochToTime(str(nextRecord[0]))
            print(timestamp)
            #hrTableWriter.logRow(str(nextRecord[0]), str(nextRecord[1]))
            hrTableWriter.logRow(timestamp, int(nextRecord[1]))
            time.sleep(1)
        else:
            print("File does not exist: " + nextFile)


# Thread to log data to the dynamic table
thread = threading.Thread(target = thread_func)
thread.start()