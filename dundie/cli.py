import argparse
import sys
from dundie.core import load

# O nome da função não necessariamente precisa se chamar 'main'
def main():
    parser = argparse.ArgumentParser(
        description='This is a Reward software',
        epilog='Use at your own risk',
    )
    parser.add_argument(
        'subcommand',
        type=str,
        help='This is a help command',
        choices=('load', 'show', 'send'),
        default='help',
    )
    parser.add_argument(
        'filepath',
        type=str,
        help='file path to load',
        default=None,
    )
    args = parser.parse_args()
    try:
        print(*globals()[args.subcommand](args.filepath))
    except KeyError:
        print('Invalid Subcommand')
        sys.exit(1)