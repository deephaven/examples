from deephaven import jpy
import os
os.system("pip install pycoingecko") #install the package to use
from pycoingecko import CoinGeckoAPI
from deephaven.TableTools import merge
from time import sleep
from deephaven.DBTimeUtils import convertDateTime, secondsToTime, millisToTime
import threading
import time

timeToWatch = 2 # minutes to keep table updating
secondsToSleep = 10 # should be 10 or higher. If too fast will hit request limit

getHistory = True
daysHistory = 90 # if getHistory = true the days to pull

#coins to get data on so far
ids=['bitcoin', 'ethereum','litecoin', 'dogecoin', 'tether', 'binancecoin','cardano', 'ripple', 'polkadot']

#tables to merge curr and prev data
tableArray=[]

DynamicTableWriter = jpy.get_type("io.deephaven.db.v2.utils.DynamicTableWriter")#org.joda.time.base.BaseDateTime works
tableWriter = DynamicTableWriter(["Coins", "DateTime", "prices", "market_caps", "total_volumes"], [jpy.get_type("java.lang.String"), jpy.get_type("io.deephaven.db.tables.utils.DBDateTime"), jpy.get_type("double"), jpy.get_type("double"), jpy.get_type("double")])

tableArray.append(tableWriter.getTable())

cg = CoinGeckoAPI()

#for historical data
if getHistory:
    for names in ids:
        coin_data_hist =cg.get_coin_market_chart_by_id(names, vs_currency="usd", days=daysHistory)
        sub = pd.DataFrame(coin_data_hist)
        tableArray.append(dataFrameToTable(sub).update("Coins = names").update("DateTime= millisToTime((long)prices_[i][0])", "prices = prices_[i][1]", "market_caps = market_caps_[i][1]", "total_volumes = total_volumes_[i][1]").moveUpColumns("Coins","DateTime"))

result = merge(tableArray).selectDistinct("DateTime", "Coins", "prices", "market_caps", "total_volumes").sortDescending("DateTime") #add each coin data to the master table
#result = result.selectDistinct("DateTime)
cg = CoinGeckoAPI()

def thread_func():
    cg = CoinGeckoAPI()
    cg.get_coins_markets(vs_currency='usd')

    for i in range(int(timeToWatch*60/secondsToSleep)):# number mins 30seconds for update times
        coin_data = cg.get_price(ids, vs_currencies='usd',
            include_market_cap=True, include_24hr_vol=True, include_24hr_change=False,include_last_updated_at=True)
        for id in ids:
            tableWriter.logRow( id, secondsToTime(int(coin_data[id]['last_updated_at'])), float(coin_data[id]['usd']), coin_data[id]['usd_market_cap'], coin_data[id]['usd_24h_vol'])


        time.sleep(secondsToSleep)# seconds to sleep
thread = threading.Thread(target=thread_func)
thread.start()
