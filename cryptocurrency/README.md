# cryptocurrency

The script has will pull live and historical for specifed cryptocurencies from the [CoinGecko](https://www.coingecko.com/) website into the Deephave Community Edition IDE.

## Variables ##
- **timeToWatch:** Integer number of minutes to run the script
- **secondsToSleep:** Integer number of seconds between data pulls.  Note that too frequent of requests will generate a HTTP status '429 Too Many Requests'. Recommend this number of 10 or higher.
- **getHistory:** Boolean value, if one wants only live data or live and historical
- **daysHistory:** Integer number of days to collect history. Data has automatic granularity. Minutely data will be used for duration within 1 day, Hourly data will be used for duration between 1 day and 90 days, Daily data will be used for duration above 90 days.
- **ids:** Array of coins to pull information. For a full and current list of values execute the following: curl -X GET "https://api.coingecko.com/api/v3/coins/list" -H "accept: application/json"




# Source and License

This script was build using the CoinGecko crypto API.  This allows one to track over 7,000 coins such as bitcoin, litecoin, ethereum, and more from more than 400 exchanges and growing.
