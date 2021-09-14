# BTC and ETH sample data

This folder contains sample data files for Bitcoin and Ethereum in CSV and Parquet format on different days.

## Table of contents

- `crypto_sept7.parquet`: Uncompressed Parquet data format of BTC and ETH.
- `crypto_sept7.csv`: CSV data format of BTC and ETH.
- `crypto_sept8.parquet`: Uncompressed Parquet data format of BTC and ETH.
- `crypto_sept8.csv`: CSV data format of BTC and ETH.

## Fields

  - **`DateTime` (DBdateTime):** The date and time that the coin value was updated.  Changes are queried every `secondsToSleep`.  Only new data will be added to the table.  If the coin value did not change, then no new data will populate.
- **`Coin` (string):** The name of the coin.
- **`low` (double):** Refers to the current low global volume-weighted average price of a coin traded on an active cryptoasset exchange as tracked by CoinGecko.
- **`high ` (double):** Refers to the current high global volume-weighted average price of a coin traded on an active cryptoasset exchange as tracked by CoinGecko.
- **`open` (double):** The prices at which a coin began in the period.
- **`close` (double):** The prices at which a coin ended in the period.
- **`volume` (double):** The number of coins traded during the period.


# Source and License

This script was built using the [CoinGecko crypto API](https://www.coingecko.com/).  This allows one to track over 7,000 coins such as bitcoin, litecoin, and ethereum from more than 400 exchanges and growing.
