# Transactions data

 [Conor O'Sullivan](https://conorosullyds.medium.com/) wrote a great article on [Batch Processing 22GB of Transaction Data with Pandas](https://towardsdatascience.com/batch-processing-22gb-of-transaction-data-with-pandas-c6267e65ff36) that discusses "[h]ow you get around limited computational resources and work with large datasets." His data set is a single CSV file of 22GB, which can be found  on [Kaggle](https://www.kaggle.com/conorsully1/simulated-transactions). You can also find his notebook, [Connor's tutorial](https://github.com/conorosully/medium-articles/blob/master/src/batch_processing.ipynb) and the [Deephaven example](https://github.com/deephaven-examples/processing-large-csv-data) on GitHub.

Using pandas with limited resources, Connor noted aggregations took about 50 minutes each.  

In this example, I'll show you how to take that example and remove pandas, also with limited resources, and use [Deephaven](https://deephaven.io/) to speed things up as much as possible.

With this code, single aggregations take _less than one minute_. With the pandas code, runtime was over 50 minutes. That's an astounding time reduction.

Here are the actual times I got on my normal laptop:

- Read Parquet Directory:  1.0 second.
- Deephaven `sum_by` expense time: 55.9 seconds.
- Deephaven `agg` expense time: 6.1 seconds.
- Deephaven monthly `sum_`  and ` avg_by` expense time: 152.9 seconds.

Note that the last one is actually several aggregations.


# Source and License

This data was built from data sets publicly available on [Kaggle](https://www.kaggle.com/conorsully1/simulated-transactions). It is provided here for demonstrative use without any warranty as to the accuracy, reliability, or completeness of the data.
