from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    from pydeephaven import Session
    session = Session()
    table1 = session.time_table(period=1000000).update(column_specs=["Col1 = i % 2"])
    df = table1.snapshot().to_pandas()
    import time
    time.sleep(5)
    return df.to_html()

app.run(port=5000, host="0.0.0.0")
