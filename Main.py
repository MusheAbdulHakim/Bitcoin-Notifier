from Cli import Cli
from notifypy import Notify
from pycoingecko import CoinGeckoAPI
import locale,schedule,time,pprint, re


class Main(object):
    def __init__(self,coin, currency='usd'):
        self.api = CoinGeckoAPI()
        self.coin = coin.lower()
        self.currency = currency.lower()

        #notification parameters
        self.icon = "./images/bitcoin.png"
        self.sound = "./sounds/gilfoyle_alert.wav"
                
    def get_latest_price(self):
        try: 
            data = self.api.get_price(ids= self.coin, vs_currencies=self.currency)
            return data[self.coin][self.currency]
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None

    def format_price(self, price):
        return locale.currency(price, grouping=True)

    def notify_me(self, price=None):
        current_price = price if price else self.get_latest_price()
        display_price = self.format_price(current_price)
        notify = Notify(
            default_notification_application_name="Crypto Alert",
            default_notification_title= f"{self.coin.title()} Price Alert", 
            default_notification_message= f"The current price is {display_price}", 
            default_notification_icon=self.icon, 
            default_notification_audio=self.sound
        )

        return notify.send()


    def list_coins(self):
        print("[+] Listing api supported crypto coins")
        coins_list = self.api.get_coins_list()
        return coins_list
    
    def list_currencies(self):
        print("[+] Listing api supported currencies")
        currencies = self.api.get_supported_vs_currencies()
        return currencies

    def get_timer(self, suffix):
        suffix = suffix.lower()
        type = 'minutes'
        if suffix == 's':
            type = 'seconds'
        if suffix =='h':
            type = 'hours'

        return type

    def start_scheduler(self, timer_str, target_price, above, below):
        digits = int(re.findall(r'\d+', timer_str)[0])
        unit = re.findall(r'[a-zA-Z]+', timer_str)[0].lower()
        
        units = {'s': 'seconds', 'm': 'minutes', 'h': 'hours'}
        method_name = units.get(unit[0], 'minutes')
        
        print(f"[*] Monitoring {self.coin.upper()} every {digits} {method_name}...")
        
        job = schedule.every(digits)
        getattr(job, method_name).do(self.alert_condition, target_price, above, below)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def alert_condition(self, target_price, above, below):

        current_price = self.get_latest_price()
        if not current_price: return
        if above and current_price >= target_price:
            self.notify_me(current_price)
        elif below and current_price <= target_price:
            self.notify_me(current_price)
        elif not above and not below:
            self.notify_me(current_price)
        

            




locale.setlocale(locale.LC_ALL, '')


if __name__ == '__main__':

    cli = Cli().parse_options()

    if cli.listcoins or cli.listcurrency:
        app = Main(cli.coin)
        pp = pprint.PrettyPrinter(indent=4, compact=True)
        if cli.listcoins:
            pp.pprint(app.list_coins())
        if cli.listcurrency:
            pp.pprint(app.list_currencies())
        exit()

    app = Main(cli.coin)
    repeat = cli.repeat

    if repeat:
        app.start_scheduler(
            timer_str=cli.time, 
            target_price=cli.price, 
            above=cli.above, 
            below=cli.below
        )
    else:
        current = app.get_latest_price()
        if cli.price:
            is_met = False
            if cli.above and current >= cli.price: is_met = True
            if cli.below and current <= cli.price: is_met = True
            
            if is_met:
                app.notify_me(current)
            else:
                print(f"Condition not met. Current: {current}, Target: {cli.price}")
        else:
            app.notify_me(current)
   