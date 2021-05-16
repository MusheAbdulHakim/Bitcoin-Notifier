import optparse

parser = optparse.OptionParser()

    
class Cli():
    def __init__(self):
       self.time = 5
       self.currency = 'usd'
       self.time_type = ''
       self.crypto = ''
       self.argument_parser()
        
    def argument_parser(self):
        parser.add_option(
            "-T",
            "--time",
            dest="time",
            help="Set timer for notifications."
        )
        parser.add_option(
            "-t",
            "--timetype",
            dest="timeType",
            help="Set timer type ('seconds' or 'minutes')."
        )
        
        parser.add_option(
            '-c',
            "--coin",
            dest="cryptoCoin",
            help="Specify the crypto currency you want."
        )
        parser.add_option(
            "--listcoins",
            dest="CoinsList",
            help="Get all supported coins."
        )

        parser.add_option(
            "--listcurrency",
            dest="listCurrencies",
            help="Get list of supported curriencies."
        )

        (options,arguments) = parser.parse_args()

        self.time = options.time
        self.time_type = options.timeType
        self.crypto = options.cryptoCoin
    

        if self.time_type != None:
            if self.time_type.lower() == 'seconds' or self.time_type.lower() == 's':
                self.time_type = 'seconds'
            if self.time_type.lower() =='minutes' or self.time_type.lower() == 'm':
                self.time_type = 'minutes'
        

        return self.time,self.time_type,self.crypto

    

