# Keysmith

Keysmith randomly chooses words from a list and concatenates them.
With a sufficiently large list, these make [decent passphrases](//xkcd.com/936) that tend to be more memorable than other random passwords.
The concept is essentially the same as (and arguably simpler than) [Diceware](//en.wikipedia.org/wiki/Diceware).

[![PyPI Version](https://img.shields.io/pypi/v/keysmith.svg)](https://pypi.python.org/pypi/keysmith)

## Installation

Keysmith is available on [PyPI](https://pypi.python.org/pypi/keysmith).

``` sh
pip install keysmith
```

## Usage

Keysmith can be run as a command-line utility.

```
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
```

Keysmith can also be imported into other Python projects.

``` python
import string
import keysmith
print(keysmith.Key(seq=string.letters, nteeth=12, delimiter=''))
```

#### Pro Tip

> Use Keysmith with KeePass and Yubikey!
