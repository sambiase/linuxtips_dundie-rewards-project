""" This is the entry point for our Program """

import argparse
import sys


def load(filepath):
    """Loads data from filepath to the DB"""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(e)


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
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print('Invalid Subcommand')
        sys.exit(1)


if __name__ == '__main__':
    main()
