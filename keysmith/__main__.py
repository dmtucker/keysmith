"""Keysmith Default Interface"""

import argparse
import math
import string

import pkg_resources

import keysmith


def cli(parser=None):
    """Parse CLI arguments and options."""
    if parser is None:
        parser = argparse.ArgumentParser(prog=keysmith.CONSOLE_SCRIPT)
    parser.add_argument(
        '-d', '--delimiter',
        help='a delimiter for the samples (teeth) in the key',
        default=' ',
    )
    parser.add_argument(
        '-n', '--nsamples',
        help='the number of random samples to take',
        type=int,
        default=3,
        dest='nteeth',
    )
    parser.add_argument(
        '-p', '--population',
        help='alphanumeric, ascii_letters, digits, printable, or a path',
        default=pkg_resources.resource_filename('keysmith', 'words.txt'),
    )
    parser.add_argument(
        '--stats',
        help='statistics for the key',
        default=False,
        action='store_true',
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s {0}'.format(keysmith.__version__),
    )
    return parser


def main(args=None):
    """Execute CLI commands."""

    if args is None:
        args = cli().parse_args()

    seq = {
        'alphanumeric': string.ascii_letters + string.digits,
        'ascii_letters': string.ascii_letters,
        'digits': string.digits,
        'printable': string.printable,
    }.get(args.population)
    if seq is None:
        with open(args.population, 'r') as f:
            seq = f.read().splitlines()

    key = keysmith.key(seq=seq, nteeth=args.nteeth, delimiter=args.delimiter)
    print(key)

    if args.stats:
        print('=' * len(key))
        print('characters = {characters}'.format(characters=len(key)))
        print('   samples = {nteeth}'.format(nteeth=args.nteeth))
        print('population = {pop}'.format(pop=len(seq)))
        print('   entropy {sign} {bits}b'.format(
            sign='<' if len(args.delimiter) < 1 else '~',
            bits=round(math.log(len(seq), 2) * args.nteeth, 2),
        ))


if __name__ == '__main__':
    main()
