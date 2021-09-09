# BTC and ETH sample data

This folder contains sample data files for Bitcoin and Ethereum in csv and parquet format on different days.

## Table of contents

- `crypto.parquet`: uncompressed parquet data format of BTC and ETH
- `crypto.csv`: csv data format of BTC and ETH

## Fields

  - **`DateTime` (DBdateTime):** The date and time that the coin value was updated.  Changes are queried every `secondsToSleep`.  Only new data will be added to the table.  If the coin value did not change, then no new data will populate.
- **`Coin` (string):** The name of the coin.
- **`price` (double):** Refers to the current global volume-weighted average price of a coin traded on an active cryptoasset exchange as tracked by CoinGecko.
- **`market_cap` (double):** One of the metrics used to measure the relative size of a coin. Market Capitalization is calculated by multiplying Coin Price with Available Supply.
- **`total_volume` (double):** The total trading volume of a coin across all active coin exchanges tracked by CoinGecko.

# Source and License

This script was built using the [CoinGecko crypto API](https://www.coingecko.com/).  This allows one to track over 7,000 coins such as bitcoin, litecoin, and ethereum from more than 400 exchanges and growing.
