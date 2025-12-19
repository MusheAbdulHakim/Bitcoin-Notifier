from Cli import Cli
from notifypy import Notify
from pycoingecko import CoinGeckoAPI
import locale,schedule,time,pprint, re


class Main(object):
    def __init__(self,coin):
        self.api = CoinGeckoAPI()
        self.coin = coin
        self.currency = 'usd'
        self.crypto = self.api.get_price(ids= self.coin, vs_currencies=self.currency)

        #notification parameters
        self.icon = "./images/bitcoin.png"
        self.sound = "./sounds/gilfoyle_alert.wav"

        self.title = f"{self.coin.title()} Current Price"
        self.message = f"The Current Price of {self.coin.title()} is {self.coin_price()}"
        

    def notify_me(self):
        notify = Notify(
            default_notification_application_name="Crypto Alert",
            default_notification_title=self.title, 
            default_notification_message=self.message, 
            default_notification_icon=self.icon, 
            default_notification_audio=self.sound
        )

        return notify.send()

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

    def getTimer(self, suffix):
        suffix = suffix.lower()
        type = 'minutes'
        if suffix == 's':
            type = 'seconds'
        if suffix =='h':
            type = 'hours'

        return type

    def startRunning(self, timer, on_loop=False):
        formatted_timer = timer.strip().replace(" ", "")
        digits = re.findall(r'\d+', formatted_timer)[0]
        unit = re.findall(r'[a-zA-Z]+', formatted_timer)[0]
        unit_method_name = self.getTimer(unit)
        print(f"Running the notifier for {(self.coin).upper()} after every {digits} {unit_method_name}")

        job = schedule.every(int(digits))
        scheduling_method = getattr(job, unit_method_name)

        scheduling_method.do(self.notify_me)
        while on_loop:
            schedule.run_pending()
            time.sleep(1)
        
        self.notify_me()




locale.setlocale(locale.LC_ALL, '')


if __name__ == '__main__':

    cli = Cli().parse_options()
    app = Main(cli.coin)
    pp = pprint.PrettyPrinter(indent=4,compact=True)

    if cli.listcoins:
        pp.pprint(app.list_coins())
        exit()
    if cli.listcurrency:
        pp.pprint(app.list_currencies())
        exit()
    
    app.startRunning(cli.time, cli.repeat)

