========
Keysmith
========

Generate passphrases by randomly selecting and concatenating words from a list.

|Build Status| |Test Coverage| |PyPI Version|

.. image:: https://imgs.xkcd.com/comics/password_strength.png

Installation
============

Use `pip <https://pip.pypa.io/>`__ to install Keysmith from `PyPI <https://pypi.org/project/keysmith/>`__.

.. code:: sh

    pip install keysmith

Usage
=====

Keysmith can be invoked from a command-line or imported in Python.

CLI
---

::

  $ keysmith --help
  usage: keysmith [-h] [-d DELIMITER] [-n NTEETH] [-p POPULATION]
                  [--encoding ENCODING] [--stats] [--version]

  optional arguments:
    -h, --help            show this help message and exit
    -d DELIMITER, --delimiter DELIMITER
                          a delimiter for the samples (teeth) in the key
                          (default: )
    -n NTEETH, --nsamples NTEETH
                          the number of random samples to take (default: 6)
    -p POPULATION, --population POPULATION
                          alphanumeric, ascii_letters, digits, printable, or a
                          path to a file of line-delimited items (default:
                          /usr/share/dict/words)
    --encoding ENCODING   the encoding of the population file (default: utf-8)
    --stats               show statistics for the key (default: False)
    --version             show program's version number and exit

::

  $ keysmith -n4
  correct horse battery staple

API
---

.. code:: python

    >>> import keysmith
    >>> help(keysmith)

.. code:: python

    >>> with open('/usr/share/dict/words', 'r') as words:
    ...     keysmith.key(seq=list(words), nteeth=4, delimiter=' ')
    ...
    'correct horse battery staple'

License
=======

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

.. |Build Status| image:: https://img.shields.io/travis/dmtucker/keysmith.svg
   :target: https://travis-ci.org/dmtucker/keysmith
.. |Test Coverage| image:: https://img.shields.io/coveralls/dmtucker/keysmith.svg
   :target: https://coveralls.io/github/dmtucker/keysmith
.. |PyPI Version| image:: https://img.shields.io/pypi/v/keysmith.svg
   :target: https://pypi.python.org/pypi/keysmith
