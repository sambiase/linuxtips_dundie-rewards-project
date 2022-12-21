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
        help='The subcommand to run',
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

    if args.subcommand == 'load':
        res = load(args.filepath)
        header = ['Name', 'Dept', 'Role', 'Email']
        for person in res:
            for key, value in zip(header,person.split(',')):
                print(f'{key} --> {value.strip()}')

