from notifypy import Notify 
import time, sched
from pycoingecko import CoinGeckoAPI

coingecko = CoinGeckoAPI()
notification = Notify()
schedule= sched.scheduler(time.time, time.sleep)

def notifyMe(title,message):
    notification.title = title
    notification.message = message
    notification.send()

def Price(coin):
    coin_price = 0
    for price in coin:
        coin_price = coin[price]
    return coin_price['usd']

bitcoin = coingecko.get_price(ids='bitcoin', vs_currencies='usd')

bitcoin_history = coingecko.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')

title = "Bitcoin Price update"
message = "The current price of bitcoin in usd is: $"+ str(Price(bitcoin))
notification.icon = "./icons/bitcoin.png"
notification.audio = "./sounds/notification.wav"

notifyMe(title,message)
schedule.enter(30, 1, notifyMe, (schedule))
schedule.run()


