import argparse

parser = argparse.ArgumentParser(description="Parse all commands parsed to the bitcoin notifier")


class Cli:
    def __init__(self):
        pass

    def parse_options(self):
        parser.add_argument(
            '-t','--time',
            type=int,default=1,
            dest='time',
            help="Set timer for notification to show. Default[1 minute]"
        )

        parser.add_argument(
            '-T','--timeType',
            type=str,default='m',
            dest='timeType',
            help="Set timer to use seconds or minutes.(s) for seconds or (m) for minutes Default [minutes]"
        )
        
        parser.add_argument(
            '-c','--coin',
            type=str,dest='coin',default='bitcoin',
            help="Set crypto currency to use. Default [bitcoin]"
        )

        parser.add_argument(
            "-L",
            "--listcoins",
            dest="listcoins",default=False,type=bool,
            help="Get all supported coins. Takes a boolearn (True or False)"
        )

        parser.add_argument(
            '-C','--currency',dest='currency',
            default='usd',type=str,
            help="Currency you want to receive notification on.Default[usd]"
        )

        parser.add_argument(
            '-l',
            "--listcurrency",
            dest="listcurrencies",default=False,type=bool,
            help="Get list of supported curriencies.Takes a boolearn (True or False)"
        )

        parser.add_argument(
            '--loop',dest="loop",default=False,
            type=bool,
            help="Repeat notification for the time set. Default [false]"
        )

        return parser.parse_args()

