from Cli import Cli
from notifypy import Notify
from pycoingecko import CoinGeckoAPI
import locale,schedule,time


class Main(object):
    def __init__(self,api,coin):
        self.api = api
        self.coin = coin
        self.currency = 'usd'
        self.crypto = self.api.get_price(ids= self.coin, vs_currencies=self.currency)
        #notification parameters
        self.notify = Notify()
        self.title = f"{self.coin.title()} Current Price"
        self.message = f"The Current Price of {self.coin.title()} is {self.coin_price()}"
        self.notify.icon = icon
        self.notify.audio = sound


    def notify_me(self):
        self.notify.title=self.title
        self.notify.message = self.message
        return self.notify.send()

    def coin_price(self):
        coin_price = 0
        for price in self.crypto:
            coin_price = self.crypto[price]
        return locale.currency(coin_price[self.currency], grouping=True)

    def list_coins(self):
        coins_list = self.api.get_coins_list()
        return coins_list
    
    def list_currencies(self):
        currencies = self.api.get_supported_vs_currencies()
        return currencies



icon = "./images/bitcoin.png"
sound = "./sounds/gilfoyle_alert.wav"



if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    cli = Cli().parse_options()
    api = CoinGeckoAPI()
    app = Main(api,cli.coin)
    
    if cli.timeType == 's':
        schedule.every(int(cli.time)).seconds.do(app.notify_me)

    schedule.every(int(cli.time)).minutes.do(app.notify_me)
    #loop for our schedules
    while True:
        schedule.run_pending()
        time.sleep(1)


