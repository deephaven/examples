# Parquet Example Data

Parquet data can be stored in many different ways - with or without metadata, in key-value partitioned directories, or in flat partitioned directories. This directory contains a simple dataset stored in all of these different formats. These are used to demonstrate Deephaven's ability to read various kinds of Parquet data.


## The `grades` dataset

The `grades` dataset is a simple synthetic dataset used to demonstrate the various ways to store Parquet data. It looks like this:

| Name | Class | Test1 | Test2 |
| ---- | ----- | ----- | ----- |
| Ashley | Math | 92 | 94 |
| Jeff | Math | 78 | 88 |
| Rita | Math | 87 | 81 |
| Zach | Math | 74 | 70 |
| Ashley | Science | 87 | 91 |
| Jeff | Science | 90 | 83 |
| Rita | Science | 99 | 95 |
| Zach | Science | 80 | 78 |
| Ashley | History | 82 | 88 |
| Jeff | History | 87 | 92 |
| Rita | History | 84 | 85 |
| Zach | History | 76 | 78 |

This dataset can be partitioned by `Name` or `Class` to demonstrate the different ways to store Parquet data.
