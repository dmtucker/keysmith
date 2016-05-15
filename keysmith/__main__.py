#!/usr/bin/env python

"""Keysmith Interface"""

import argparse
import math
import os
import string
import sys

from keysmith import __version__
from keysmith import Key


def cli(parser=argparse.ArgumentParser(prog='keysmith')):
    """Parse CLI arguments and options."""
    parser.add_argument(
        '-d', '--delimiter',
        help='a delimiter for the samples (teeth) in the key',
        default=' '
    )
    parser.add_argument(
        '-n', '--nsamples',
        help='the number of random samples to take',
        type=int,
        default=3
    )
    parser.add_argument(
        '-p', '--population',
        help='alphanumeric, default, printable, or a path',
        default='default'
    )
    parser.add_argument(
        '--stats',
        help='statistics for the key',
        default=False,
        action='store_true'
    )
    parser.add_argument(
        '--version',
        help='Keysmith v{version}'.format(version=__version__),
        default=False,
        action='store_true'
    )
    return parser


def main():
    """Execute CLI commands."""
    args = cli().parse_args()
    if args.version:
        print(__version__)
        sys.exit(0)
    words = {
        'alphanumeric': string.ascii_letters + string.digits,
        'printable': string.printable,
    }.get(args.population)
    if words is None:
        if args.population == 'default':
            args.population = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                'words.txt'
            )
        with open(args.population, 'r') as f:
            words = f.read().splitlines()
    key = Key(
        seq=words,
        nteeth=args.nsamples,
        delimiter=args.delimiter
    )
    print(key)
    if args.stats:
        print('=' * len(key))
        print('characters = {characters}'.format(characters=len(key)))
        print('   samples = {nteeth}'.format(nteeth=args.nsamples))
        print('population = {pop}'.format(pop=len(words)))
        print('   entropy {sign} {bits}b'.format(
            sign='<' if len(args.delimiter) < 1 else '~',
            bits=round(math.log(len(words), 2) * args.nsamples, 2)
        ))


if __name__ == '__main__':
    main()
