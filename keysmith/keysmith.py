from __future__ import absolute_import

import random

class Key(str):

    class Tooth(str):

        def __new__(self, seq):
            return random.SystemRandom().choice(seq).strip()

    def __new__(self, seq, nteeth=6, delimiter=' '):
        return delimiter.join([self.Tooth(seq) for i in range(nteeth)])
