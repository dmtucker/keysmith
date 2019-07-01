========
Keysmith
========

Generate passphrases by randomly selecting and concatenating words from a list.

**Note: This project is no longer maintained.**
Use `xkcdpass <https://pypi.org/project/xkcdpass>`__ instead.

.. image:: https://imgs.xkcd.com/comics/password_strength.png
   :target: https://xkcd.com/936/

Installation
============

Use `pip <https://pip.pypa.io/>`__ to install Keysmith.

.. code:: sh

    pip install keysmith

Usage
=====

Keysmith can be invoked from a command-line or imported in Python.

CLI
---

::

  $ keysmith --help
  usage: keysmith [-h] [--delimiter DELIMITER] [--encoding ENCODING]
                  [--nsamples NTEETH] [--population POPULATION] [--stats]
                  [--version]

  optional arguments:
    -h, --help            show this help message and exit
    --delimiter DELIMITER
                          a delimiter for the samples (teeth) in the key
                          (default: )
    --encoding ENCODING   the encoding of the population file (default: utf-8)
    --nsamples NTEETH, -n NTEETH
                          the number of random samples to take (default: 6)
    --population POPULATION, -p POPULATION
                          alphanumeric, ascii_letters, digits, printable, or a
                          path to a file of line-delimited items (default:
                          /usr/share/dict/words)
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
