from notifypy import Notify 
import time, schedule,optparse
from pycoingecko import CoinGeckoAPI


class App():
    def __init__(self):
        self.coingecko = CoinGeckoAPI()
        self.notification = Notify()
        self.bitcoin = self.coingecko.get_price(ids='bitcoin', vs_currencies='usd')
        self.title = "Bitcoin Current Price"
        self.message = "The current price of bitcoin in usd is: $"+ str(self.Price(self.bitcoin))
        self.notification.icon = "./icons/bitcoin.png"
        self.notification.audio = "./sounds/notification.wav"

    def notifyMe(self):
        self.notification.title = self.title
        self.notification.message = self.message
        self.notification.send()

    def Price(self,coin):
        coin_price = 0
        for price in coin:
            coin_price = coin[price]
        return coin_price['usd']

#instantiate our app class
app = App()
parser = optparse.OptionParser()


try:
    #returns the notification which is callable as required by schedule
    def get_notification():
        return app.notifyMe()

    parser.add_option("-t","--time",dest="time",help="Time in (minutes) you want to be receiving notifications.")
    (options,arguments) = parser.parse_args()
    notify_time = int(options.time)

    #call get_notification function to the schedule
    if notify_time:
        schedule.every(notify_time).minutes.do(get_notification)
    schedule.every(1).minutes.do(get_notification)
    #loop for our schedules
    while True:
        schedule.run_pending()
        time.sleep(1)

except Exception as exception:
    print(exception.with_traceback())
