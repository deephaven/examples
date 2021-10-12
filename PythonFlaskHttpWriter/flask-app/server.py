from flask import Flask
from pydeephaven import Session

app = Flask(__name__)
session = Session()

init = """
from deephaven import DynamicTableWriter
import deephaven.Types as dht

table_writer = DynamicTableWriter(
    ["A"],
    [dht.int_]
)

table = table_writer.getTable()
"""

update_template = """
def update(x):
    table_writer.logRow(x)

update({value})
"""

session.run_script(init)

@app.route('/')
def hello():
    session.run_script(update_template.format(value="3"))
    return "Request received"

app.run(port=5000, host="0.0.0.0")
