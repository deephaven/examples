# CryptoCurrency

The script will pull live and historical data for specified cryptocurrencies from the [CoinGecko](https://www.coingecko.com/) website into [Deephaven](https://github.com/deephaven/deephaven-core).


## How it works

### Deephaven application mode

This app runs using [Deephaven's application mode](https://deephaven.io/core/docs/how-to-guides/app-mode/).

### Components
* `Dockerfile` - The dockerfile for the application. This extends the default Deephaven image to add dependencies. See our guide, [How to install Python packages](https://deephaven.io/core/docs/how-to-guides/install-python-packages/#add-packages-to-a-custom-docker-image), for more information.
* `docker-compose.yml` - The Docker Compose file for the application. This is mostly the same as the [Deephaven docker-compose file](https://raw.githubusercontent.com/deephaven/deephaven-core/main/containers/python-examples/docker-compose.yml), with modifications to run in application mode.
* `start.sh` - A simple helper script to launch the application.
* `app.d/cryptoApp.app` - The Deephaven application mode app file.
* `app.d/crypto.py` - The Python script that pulls the data from [CoinGecko](https://www.coingecko.com/) and stores it into Deephaven.
* `crypto.png` - Image of the end state of Deephaven tables.


### High level overview

This app pulls data from [CoinGecko](https://www.coingecko.com/) through HTTP requests. The API responses are deserialized, and the desired values are extracted and stored in a Deephaven table.

Once data is collected and tables are created, various Deephaven queries are then performed on the tables. See the [Deephaven Community Core documentation](https://deephaven.io/core/docs/) to learn more about these methods.

This app writes to Deephaven tables both statically and dynamically.

## Dependencies

* The [Deephaven-core dependencies](https://github.com/deephaven/deephaven-core#required-dependencies) are required for this project.

## Launch

Before launching, you can modify the `ids` and `daysHistory` values in `crypto.py`.

Once you are set, simply run the following to launch the app:

```
sh start.sh
```

Go to [http://localhost:10000/ide](http://localhost:10000/ide) to view the tables in the top right **Panels** tab!

## Variables
- **`secondsToSleep`:** Integer number of seconds between data pulls.  It is recommended that this number is 10 or higher. Note that too frequent requests will generate an HTTP status: '429 Too Many Requests'. The [CoinGecko free API](https://www.coingecko.com/en/api/documentation) has a rate limit of 50 calls/minute.
- **`daysHistory`:** Integer number of days to collect history. Data has automatic granularity.
   - Minutely data will be returned for a duration within 1 day.
   - Hourly data will be returned for a duration between 1 day and 90 days.
   - Daily data will be returned for a duration above 90 days.
- **`ids`:** Array of coins to pull information on. For a full and current list of values, execute the following: `curl -X GET "https://api.coingecko.com/api/v3/coins/list" -H "accept: application/json"`

# Outcome

Upon running the script in your Deephaven IDE, the `HistoricalCryptoTable` and `LiveCryptoTable` tables will be created.  


![img](./crypto1.png)

The result table includes the following columns:

- **`Timestamp`:** The date and time that the coin value was updated.
- **`Coin`:** The name of the coin.
- **`Price`:** Refers to the current global volume-weighted average price of a coin traded on an active cryptoasset exchange as tracked by CoinGecko.
- **`MarketCap`:** One of the metrics used to measure the relative size of a coin. Market Capitalization is calculated by multiplying Coin Price with Available Supply.
- **`TotalVolume`:** The total trading volume of a coin across all active coin exchanges tracked by CoinGecko.


# Source and License

This script was built using the [CoinGecko crypto API](https://www.coingecko.com/).  This allows one to track over 7,000 coins such as bitcoin, litecoin, and ethereum from more than 400 exchanges and growing.
