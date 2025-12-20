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
            '-C','--currency',
            dest='currency',
            default='usd',
            type=str,
            help="Currency you want to receive notification on.Default[usd]"
        )

        parser.add_argument(
            '-p',
            '--price',
            type=float,
            help="Set a price point."
        )

        parser.add_argument(
            '-b',
            '--below',
            dest='below',
            action='store_true',
            help="Only receive the notification if the current price goes below the price set with --price."
        )
        parser.add_argument(
            '-a',
            '--above',
            dest='above',
            action='store_true',
            help="Only receive the notification if the current price goes above the price set with --price."
        )

        parser.add_argument(
            "-L",
            "--listcoins",
            dest="listcoins",
            action='store_true',
            help="Get all supported coins."
        )

        parser.add_argument(
            '-l',
            "--listcurrency",
            action='store_true',
            help="Get list of supported curriencies."
        )

        parser.add_argument(
            '-r',
            '--repeat',
            default= False,
            action='store_true',
            help="Repeat notification for the time set. Default [False]"
        )

        return parser.parse_args()
