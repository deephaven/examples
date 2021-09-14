# Cryptocurrency

The script will pull live and historical data for specified cryptocurencies from the [CoinGecko](https://www.coingecko.com/) website into [Deephaven](https://github.com/deephaven/deephaven-core).

## Variables
- **`timeToWatch`:** Integer number of minutes to run the script.
- **`secondsToSleep`:** Integer number of seconds between data pulls.  It is recommended that this number is 10 or higher. Note that too frequent requests will generate an HTTP status: '429 Too Many Requests'.
- **`getHistory`:** Boolean value.
   -  `false` for only live data.
   -  `true` for live and historical data.
- **`daysHistory`:** Integer number of days to collect history. Data has automatic granularity. 
   - Minutely data will be returned for a duration within 1 day.
   - Hourly data will be returned for a duration between 1 day and 90 days.
   - Daily data will be returned for a duration above 90 days.
- **`ids`:** Array of coins to pull information on. For a full and current list of values, execute the following: `curl -X GET "https://api.coingecko.com/api/v3/coins/list" -H "accept: application/json"`

# Outcome

Upon running the script in your Deephaven IDE, the `result` table will be created.  

This table can be sorted on the `Timestamp` column to see new data streaming in.

![img](./crypto1.png)

The result table includes the following columns:

- **`Timestamp`:** The date and time that the coin value was updated.
- **`Coin`:** The name of the coin.
- **`Price`:** Refers to the current global volume-weighted average price of a coin traded on an active cryptoasset exchange as tracked by CoinGecko.
- **`MarketCap`:** One of the metrics used to measure the relative size of a coin. Market Capitalization is calculated by multiplying Coin Price with Available Supply.
- **`total_volume`:** The total trading volume of a coin across all active coin exchanges tracked by CoinGecko.


# Source and License

This script was built using the [CoinGecko crypto API](https://www.coingecko.com/).  This allows one to track over 7,000 coins such as bitcoin, litecoin, and ethereum from more than 400 exchanges and growing.
