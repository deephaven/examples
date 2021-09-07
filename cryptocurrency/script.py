import os
os.system("pip install pycoingecko") 

from pycoingecko import CoinGeckoAPI

from deephaven.DBTimeUtils import secondsToTime, millisToTime
from deephaven.TableTools import merge
from deephaven import DynamicTableWriter
import deephaven.Types as dht


from time import sleep, time
import pandas as pd
import threading


# minutes to query crypto prices
timeToWatch = 2 

# secondsToSleep should be 10 or higher. If too fast, will hit request limit.
secondsToSleep = 10 


getHistory = False

# if getHistory = true, the days to pull
daysHistory = 90 

# coins to get data
ids=['bitcoin', 'ethereum','litecoin', 'dogecoin', 'tether', 'binancecoin', 'cardano', 'ripple', 'polkadot']

# array to store tables for current and previous data
tableArray=[]

tableWriter = DynamicTableWriter(["coin", "dateTime", "price", "marketCap", "totalVolume"], [dht.string, dht.datetime, dht.double, dht.double, dht.double])


tableArray.append(tableWriter.getTable())

cg = CoinGeckoAPI()

# get historical data
if getHistory:
    for names in ids:
        coin_data_hist = cg.get_coin_market_chart_by_id(names, vs_currency = "usd", days = daysHistory)
        sub = pd.DataFrame(coin_data_hist)
        tableArray.append(dataFrameToTable(sub).view("dateTime = millisToTime((long)prices_[i][0])", "coin = names", "price = prices_[i][1]", "marketCap = market_caps_[i][1]", "totalVolume = total_volumes_[i][1]").moveUpColumns("dateTime", "coin"))

#add each coin data to the master table
result = merge(tableArray).selectDistinct("dateTime", "coin", "price", "marketCap", "totalVolume").sortDescending("dateTime") 

def thread_func():

    cg.get_coins_markets(vs_currency = 'usd')

    for i in range(int(timeToWatch*60/secondsToSleep)):
        coin_data = cg.get_price(ids, vs_currencies = 'usd', include_market_cap = True, include_24hr_vol = True, include_24hr_change = False, include_last_updated_at = True)

        for id in ids:
            #Add new data to the dynamic table
            tableWriter.logRow( id, secondsToTime(int(coin_data[id]['last_updated_at'])), float(coin_data[id]['usd']), coin_data[id]['usd_market_cap'], coin_data[id]['usd_24h_vol'])

        sleep(secondsToSleep)

thread = threading.Thread(target = thread_func)
thread.start()
