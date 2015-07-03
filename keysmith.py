#!/usr/bin/env python


import argparse
import os
import random
import sys


class Keysmith:

    words = None

    def __init__(self, words):
        self.words = words

    def generate(self, degree):
        key = ''
        for i in range(degree):
            key += random.SystemRandom().choice(self.words).strip()
        return key


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--degree',
        help='Specify the number of words to include.',
        type=int,
        default=3
    )
    parser.add_argument(
        '-q', '--quantity',
        help='Specify the number of keys to generate.',
        type=int,
        default=1
    )
    parser.add_argument(
        '-w', '--words',
        help='Specify the word list to use.',
        default=os.path.join(os.path.dirname(sys.argv[0]), 'word.list')
    )
    args = parser.parse_args()

    with open(args.words, 'r') as f:
        words = f.readlines()
    for i in range(args.quantity):
        print(Keysmith(words).generate(args.degree))
