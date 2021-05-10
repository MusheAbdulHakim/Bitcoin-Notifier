from notifypy import Notify 
import time, schedule
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

#returns the notification which is callable as required by schedule
def get_notification():
    return app.notifyMe()

#call get_notification function to the schedule
schedule.every(1).minutes.do(get_notification)

#schedule for seconds below
#schedule.every(1).seconds.do(get_notification)

#loop for our schedules
while True:
    schedule.run_pending()
    time.sleep(1)


