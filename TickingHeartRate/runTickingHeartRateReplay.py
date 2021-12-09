from deephaven import read_csv
from deephaven import DynamicTableWriter, Types as dht
from deephaven import DateTimeUtils
import pathlib
import time
import threading

# Max number of csv files to pull in
csv_files=500

# Setup deephaven tables to hold heart rate results
column_names = ["Timestamp", "HeartRate"]
column_types = [dht.datetime, dht.int_]
hr_table_writer = DynamicTableWriter(column_names, column_types)
heart_rate_data = hr_table_writer.getTable()

# Function to log data to the dynamic table
def thread_func():
    for x in range(1, csv_files):
        next_file = ("/data/examples/TickingHeartRate/csv/%d.csv" % x)
        print(next_file)
        path = pathlib.Path(next_file)
        if path.exists() and path.is_file():
            next_hr = read_csv(next_file, headless = True).view("Timestamp=Column1", "HeartRate=Column2")
            next_record = next_hr.getRecord(0, "Timestamp", "HeartRate")
            timestamp = next_record[0]
            hr_table_writer.logRow(timestamp, int(next_record[1]))
            time.sleep(1)
        else:
            print("File does not exist: " + next_file)

# Thread to log data to the dynamic table
thread = threading.Thread(target = thread_func)
thread.start()