# Synthcity data

This folder contains data files from [Synthcity](http://www.synthcity.xyz/download.html)

With deep learning becoming a more prominent approach for automatic classification of three-dimensional point cloud data, a key bottleneck is the amount of high quality training data, especially when compared to that available for two-dimensional images. One potential solution is the use of synthetic data for pre-training networks, however the ability for models to generalize from synthetic data to real world data has been poorly studied for point clouds. Despite this, a huge wealth of 3D virtual environments exist which, if proved effective can be exploited. We therefore argue that research in this domain would be of significant use. In this paper we present SynthCity an open dataset to help aid research. SynthCity is a synthetic full color Mobile Laser Scanning point cloud. Every point is assigned a label from one of nine categories. We generate our point cloud in a typical Urban/Suburban environment using the Blensor plugin for Blender.

## Table of contents

- `parquet`: directory containing partitioned parquet data

## Fields

  - **X (double):**  X coordinate of the point.
  - **Y (double):**  Y coordinate of the point.
  - **Z (double):**  Z coordinate of the point.
  - **X_noise (double):**  X coordinate of the point used in noise calculation.
  - **Y_noise (double):**  Y coordinate of the point used in noise calculation.
  - **Z_noise (double):**  Z coordinate of the point used in noise calculation.
  - **R (double):** Red value of the point.
  - **G (double):** Green value of the point.
  - **B (double):** Blue value of the point.
  - **time (double):**  Global navigation satellite system time of syntetic measurement.
  - **eol (boolean):**  The end of line is calculated as a binary indicator where eol = 1 if it is the final point acquired by the individual scan or eol = 0 otherwise.
  - **label (double):**  0 - 9, label representing the sub location.

# Source and License

This data was built from data sets publicly available on [Synthcity](https://arxiv.org/pdf/1907.04758.pdf). It is provided here for demonstrative use without any warranty as to the accuracy, reliability, or completeness of the data.
