import optparse

parser = optparse.OptionParser()

    
class Cli():
   
    def __init__(self,  time='1m', currency = 'usd', crypto= 'bitcoin'):
       self.time = time
       self.currency = currency
       self.getCurrencies = False
       self.getCoins = False
       self.crypto = crypto
       self.argument_parser()
        
    def argument_parser(self):
        parser.add_option(
            "-t",
            "--time",
            dest="time",
            help="Set timer for notifications. Example: 1m to set the timer to every 1 minute"
        )

        
        parser.add_option(
            '-c',
            "--coin",
            dest="cryptoCoin",
            help="Specify the crypto currency you want."
        )
        parser.add_option(
            "-L",
            "--listcoins",
            dest="CoinsList",
            help="Get all supported coins. Takes a boolearn (True or False)"
        )

        parser.add_option(
            '-l',
            "--listcurrency",
            dest="Currencies",
            help="Get list of supported curriencies.Takes a boolearn (True or False)"
        )

        (options,arguments) = parser.parse_args()

        if options.time != None:
            self.time = options.time
        if options.cryptoCoin != None:
            self.crypto = options.cryptoCoin

        get_coins = options.CoinsList
        get_currencies = options.Currencies

        if get_coins != None:
            self.getCoins = get_coins
        if get_currencies != None:
            self.getCurrencies = get_currencies

        return self.time,self.crypto,self.getCurrencies,self.getCoins

    

