# Cryptocurrency

The script will pull live and historical data for specified cryptocurencies from the [CoinGecko](https://www.coingecko.com/) website into the Deephaven Community Core IDE.

## Variables
- **timeToWatch:** Integer number of minutes to run the script.
- **secondsToSleep:** Integer number of seconds between data pulls.  Note that too frequent of requests will generate an HTTP status '429 Too Many Requests'. It is recommended that this number does not exceed 10 or higher.
- **getHistory:** Boolean value, 
   -  `false` if one wants only live data.
   -  `true` if one wants live and historical data.
- **daysHistory:** Integer number of days to collect history. Data has automatic granularity. 
   - Minutely data will be used for a duration within 1 day.
   - Hourly data will be used for a duration between 1 day and 90 days.
   - Daily data will be used for a duration above 90 days.
- **ids:** Array of coins to pull information. For a full and current list of values execute the following: `curl -X GET "https://api.coingecko.com/api/v3/coins/list" -H "accept: application/json"`


# Outcome

Upon running the script in your Deephaven IDE the `results` table will be created.  

This table can be sorted on the DateTime column to see new data streaming in.

![img](./crypto1.png)


# Source and License

This script was built using the CoinGecko crypto API.  This allows one to track over 7,000 coins such as bitcoin, litecoin, and ethereum from more than 400 exchanges and growing.
