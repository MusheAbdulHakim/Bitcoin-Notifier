from notifypy import Notify
import time, schedule,locale,pprint
from cli import Cli
from pycoingecko import CoinGeckoAPI

class App():
    def __init__(self,api,crypto_coin):
        self.coingecko = api
        self.notification = Notify()
        self.crypto_coin = crypto_coin  
        self.currency = 'usd'
        self.crypto = self.coingecko.get_price(ids=self.crypto_coin, vs_currencies=self.currency)
        self.title = f"{self.crypto_coin.title()} Current Price"
        self.message = f"The Current Price of {self.crypto_coin.title()} is {self.Price()}"
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

    def getCoinList(self):
        coins_list = self.coingecko.get_coins_list()
        return coins_list
    
    def getCurrencies(self):
        currencies = self.coingecko.get_supported_vs_currencies()
        return currencies


locale.setlocale(locale.LC_ALL, '')
icon = "./images/bitcoin.png"
sound = "./sounds/gilfoyle_alert.wav"

cli = Cli()

time_type = cli.time_type
notify_time = cli.time
crypto_currency = cli.crypto

if cli.time == None:
    notify_time = 1

if cli.time_type == None:
    time_type = 'minutes'

if cli.crypto == None:
    crypto_currency = 'bitcoin'

api = CoinGeckoAPI()
app = App(api,crypto_currency)
pp = pprint.PrettyPrinter(indent=4,compact=True)
if cli.getCoins:
    pp.pprint(app.getCoinList())

if cli.getCurrencies:
    pp.pprint(app.getCurrencies())

def get_notification():
    return app.notifyMe()


try:
    if time_type =='seconds':
        schedule.every(int(notify_time)).seconds.do(get_notification)

    schedule.every(int(notify_time)).minutes.do(get_notification)

        #loop for our schedules
    while True:
        schedule.run_pending()
        time.sleep(1)

except Exception as e:
    print(e)