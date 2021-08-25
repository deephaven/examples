#install the package to use
import os
os.system("pip install pycoingecko") 

from pycoingecko import CoinGeckoAPI

from deephaven.DBTimeUtils import secondsToTime, millisToTime
from deephaven.TableTools import merge
from deephaven import DynamicTableWriter
import deephaven.types as dht

from time import sleep
import threading
import pandas as pd

timeToWatch = 2 # minutes to query crypto prices
secondsToSleep = 10 # should be 10 or higher. If too fast will hit request limit

getHistory = True
daysHistory = 90 # if getHistory = true the days to pull

#coins to get data
ids=['bitcoin', 'ethereum','litecoin', 'dogecoin', 'tether', 'binancecoin', 'cardano', 'ripple', 'polkadot']

# array of current and previous data
tableArray=[]

DynamicTableWriter = jpy.get_type("io.deephaven.db.v2.utils.DynamicTableWriter")
tableWriter = DynamicTableWriter(["coin", "dateTime", "price", "marketCap", "totalVolume"], [dht.string, dht.DBDateTime, dht.double, dht.double, dht.double])

tableArray.append(tableWriter.getTable())

cg = CoinGeckoAPI()

# get historical data
if getHistory:
    for names in ids:
        coin_data_hist = cg.get_coin_market_chart_by_id(names, vs_currency="usd", days=daysHistory)
        sub = pd.DataFrame(coin_data_hist)
        tableArray.append(dataFrameToTable(sub).update("coin = names").update("dateTime= millisToTime((long)prices_[i][0])", "price = prices_[i][1]", "marketCap = market_caps_[i][1]", "totalVolume = total_volume_[i][1]").moveUpColumns("Coin","DateTime"))

#add each coin data to the master table
result = merge(tableArray).selectDistinct("dateTime", "coin", "price", "marketCap", "totalVolume").sortDescending("DateTime") 

def thread_func():
    cg = CoinGeckoAPI()
    cg.get_coins_markets(vs_currency='usd')

    for i in range(int(timeToWatch*60/secondsToSleep)):
        coin_data = cg.get_price(ids, vs_currencies='usd',
            include_market_cap=True, include_24hr_vol=True, include_24hr_change=False,include_last_updated_at=True)

            for id in ids:
            tableWriter.logRow( id, secondsToTime(int(coin_data[id]['last_updated_at'])), float(coin_data[id]['usd']), coin_data[id]['usd_market_cap'], coin_data[id]['usd_24h_vol'])


        time.sleep(secondsToSleep)
thread = threading.Thread(target=thread_func)
thread.start()
