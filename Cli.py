import argparse

parser = argparse.ArgumentParser(description="Parse all commands parsed to the bitcoin notifier")


class Cli:
    def parse_options(self):
        parser.add_argument(
            '-t','--time',
            type=str,
            default='1m',
            dest='time',
            help="Set timer for notification to show. Default[1 minute]"
        )

        
        parser.add_argument(
            '-c','--coin',
            type=str,
            dest='coin',
            default='bitcoin',
            help="Set crypto currency to use. Default [bitcoin]"
        )

        parser.add_argument(
            "-L",
            "--listcoins",
            dest="listcoins",
            default=False,
            type=bool,
            help="Get all supported coins. Takes a boolean (True or False)"
        )

        parser.add_argument(
            '-C','--currency',
            dest='currency',
            default='usd',
            type=str,
            help="Currency you want to receive notification on.Default[usd]"
        )

        parser.add_argument(
            '-l',
            "--listcurrency",
            action='store_true',
            help="Get list of supported curriencies.Takes a boolean (True or False)"
        )

        parser.add_argument(
            '-r',
            '--repeat',
            default= True,
            action='store_true',
            help="Repeat notification for the time set. Default [True]"
        )

        return parser.parse_args()
