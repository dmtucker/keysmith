#!/usr/bin/env python

import argparse
import os
import random
import sys


def natural_number(x):
    if x != int(x) or x < 0:
        raise argparse.ArgumentTypeError(str(x) + ' is not a natural number.')
    return x


def random_word(words):
    """ Generate a random word. """
    return random.SystemRandom().choice(words).strip()


def random_key(words, degree):
    """ Generate a random key. """
    key = ''
    for i in range(degree):
        key += random_word(words)
    return key


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--degree',
        help='Specify the number of words to include.',
        type=natural_number,
        default=3
    )
    parser.add_argument(
        '-s', '--source',
        help='Specify the word list to use.',
        default=os.path.join(os.path.dirname(sys.argv[0]), 'word.list')
    )
    args = parser.parse_args()
    with open(args.source, 'r') as source:
        words = source.readlines()
    print(random_key(words, args.degree))
