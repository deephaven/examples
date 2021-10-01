from pycoingecko import CoinGeckoAPI

from deephaven.DBTimeUtils import secondsToTime, millisToTime
from deephaven.TableTools import merge
from deephaven import DynamicTableWriter

import deephaven.Types as dht
import jpy

from time import sleep, time
import pandas as pd
import threading

# secondsToSleep should be 10 or higher. If too fast, will hit request limit.
secondsToSleep = 60

# if getHistory = true, the days to pull
daysHistory = 90

# coins to get data
ids = ['bitcoin', 'ethereum', 'litecoin', 'dogecoin', 'tether', 'binancecoin', 'cardano', 'ripple', 'polkadot']

getLive = True

getHistory = True

# below this line there are no variables that need changed
########################################################################

def get_coingecko_table_historical(daysHistory = 90):
    tableArray = []
    cg = CoinGeckoAPI()

    # get historical data
    for id in ids:
        coin_data_hist = cg.get_coin_market_chart_by_id(id, vs_currency = "usd", days = daysHistory)
        sub = pd.DataFrame(coin_data_hist)
        coin_query = "Coin = `{id}`".format(id=id)
        tableArray.append(dataFrameToTable(sub).view("DateTime = millisToTime((long)prices_[i][0])", coin_query, "Price = prices_[i][1]", "MarketCap = market_caps_[i][1]", "TotalVolume = total_volumes_[i][1]").moveUpColumns("DateTime", "Coin"))
    return merge(tableArray).selectDistinct("DateTime", "Coin", "Price", "MarketCap", "TotalVolume").sortDescending("DateTime", "Coin")


def get_coingecko_table_live(secondsToSleep = 60):
    cg = CoinGeckoAPI()

    # array to store tables for current and previous data
    tableArray=[]

    tableWriter = DynamicTableWriter(['Coin', 'DateTime', 'Price', 'MarketCap', 'TotalVolume'], [dht.string, dht.datetime, dht.double, dht.double, dht.double])

    tableArray.append(tableWriter.getTable())
    result = merge(tableArray).selectDistinct('DateTime', 'Coin', 'Price', 'MarketCap', 'TotalVolume').sortDescending('DateTime', 'Coin')

    def thread_func():
        cg.get_coins_markets(vs_currency = 'usd')

        while True:
            coin_data = cg.get_price(ids, vs_currencies = 'usd', include_market_cap = True, include_24hr_vol = True, include_24hr_change = False, include_last_updated_at = True)

            for id in ids:
                #Add new data to the dynamic table
                tableWriter.logRow( id, secondsToTime(int(coin_data[id]['last_updated_at'])), float(coin_data[id]['usd']), coin_data[id]['usd_market_cap'], coin_data[id]['usd_24h_vol'])

            sleep(secondsToSleep)

    thread = threading.Thread(target = thread_func)
    thread.start()
    return result

if getHistory:
    HistoricalCryptoTable = get_coingecko_table_historical(daysHistory)

if getLive:
    LiveCryptoTable = get_coingecko_table_live(secondsToSleep)
