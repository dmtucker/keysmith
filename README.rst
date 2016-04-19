Keysmith
========

Keysmith randomly chooses words from a list and concatenates them. With
a sufficiently large list, these make `decent
passphrases <//xkcd.com/936>`__ that tend to be more memorable than
other random passwords. The concept is essentially the same as (and
arguably simpler than) `Diceware <//en.wikipedia.org/wiki/Diceware>`__.

|PyPI Version|

Installation
------------

Keysmith is available on
`PyPI <https://pypi.python.org/pypi/keysmith>`__.

.. code:: sh

    pip install keysmith

Usage
-----

Keysmith can be run as a command-line utility.

::

    $ keysmith --help
    usage: keysmith [-h] [-d DELIMITER] [-n NSAMPLES] [-p POPULATION] [--stats]
                    [--version]

    optional arguments:
      -h, --help            show this help message and exit
      -d DELIMITER, --delimiter DELIMITER
                            a delimiter for the samples (teeth) in the key
      -n NSAMPLES, --nsamples NSAMPLES
                            the number of random samples to take
      -p POPULATION, --population POPULATION
                            alphanumeric, default, local, printable, or a path
      --stats               statistics for the key
      --version             keysmith 0.2.1
    $ keysmith -n 4
    correct horse battery staple

Keysmith can also be imported into other Python projects.

.. code:: python

    import string
    import keysmith
    print(keysmith.Key(seq=string.letters, nteeth=12, delimiter=''))

Pro Tip
~~~~~~~

    Use Keysmith with KeePass and Yubikey!

.. |PyPI Version| image:: https://img.shields.io/pypi/v/keysmith.svg
   :target: https://pypi.python.org/pypi/keysmith

License
-------

Copyright (C) 2016 David Tucker

This library is free software; you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or (at
your option) any later version.

This library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this library; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
