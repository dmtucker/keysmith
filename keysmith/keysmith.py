"""Key Definition"""

import random


class Key(str):

    """A Secret String Composed of Teeth"""

    class Tooth(str):

        """A Piece of a Key"""

        def __new__(cls, seq):
            return random.SystemRandom().choice(seq).strip()

    def __new__(cls, seq, nteeth=6, delimiter=' '):
        return delimiter.join([cls.Tooth(seq) for _ in range(nteeth)])
