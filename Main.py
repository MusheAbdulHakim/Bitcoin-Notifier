from Cli import Cli
from notifypy import Notify
from pycoingecko import CoinGeckoAPI
import locale,schedule,time,pprint


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
        print("[+] Listing api supported crypto coins")
        coins_list = self.api.get_coins_list()
        return coins_list
    
    def list_currencies(self):
        print("[+] Listing api supported currencies")
        currencies = self.api.get_supported_vs_currencies()
        return currencies



icon = "./images/bitcoin.png"
sound = "./sounds/gilfoyle_alert.wav"
locale.setlocale(locale.LC_ALL, '')


if __name__ == '__main__':

    cli = Cli().parse_options()
    api = CoinGeckoAPI()
    app = Main(api,cli.coin)
    pp = pprint.PrettyPrinter(indent=4,compact=True)

    if cli.listcoins:
        pp.pprint(app.list_coins())
        exit()
    if cli.listcurrencies:
        pp.pprint(app.list_currencies())
        exit()
    
    if cli.loop:
        if cli.timeType[0].lower() == 's':
            schedule.every(int(cli.time)).seconds.do(app.notify_me)
        elif cli.timeType[0].lower() == 'm':
            schedule.every(int(cli.time)).minutes.do(app.notify_me)
        #loop for our schedules
        while True:
            schedule.run_pending()
            time.sleep(1)
    app.notify_me()

