from notifypy import Notify
import time, schedule,optparse,locale
from pycoingecko import CoinGeckoAPI

class App():
    def __init__(self,crypto_coin):
        self.coingecko = CoinGeckoAPI()
        self.notification = Notify()
        locale.setlocale(locale.LC_ALL, '')
        self.crypto_coin = crypto_coin  
        self.currency = 'usd'
        self.crypto = self.coingecko.get_price(ids=self.crypto_coin, vs_currencies=self.currency)
        self.title = "Bitcoin Current Price"
        self.message = f"The current price of {self.crypto_coin} is {self.Price()}"
        self.notification.icon = icon
        self.notification.audio = sound

    def notifyMe(self):
        self.notification.title = self.title
        self.notification.message = self.message
        self.notification.send()

    def Price(self):
        coin_price = 0
        for price in self.crypto:
            coin_price = self.crypto[price]
        return locale.currency(coin_price[self.currency], grouping=True) 


icon = "./icons/bitcoin.png"
sound = "./sounds/notification.wav"
parser = optparse.OptionParser()

parser.add_option("-t","--time",dest="time",help="Time in (minutes) you want to be receiving notifications.")
parser.add_option('-c',"--coin",dest="crypto",help="Crypto currency price you want.")
(options,arguments) = parser.parse_args()
notify_time = options.time

CRYPTO_CURRENCY = 'bitcoin'

if options.crypto:
    CRYPTO_CURRENCY = options.crypto

app = App(CRYPTO_CURRENCY.lower())


def get_notification():
    return app.notifyMe()

try:
    
    #call get_notification function to the schedule
    if notify_time:
        schedule.every(int(notify_time)).minutes.do(get_notification)
    schedule.every(1).minutes.do(get_notification)
    # schedule.every(10).seconds.do(get_notification)
    #loop for our schedules
    while True:
        schedule.run_pending()
        time.sleep(1)

except Exception as exception:
    print(exception)
