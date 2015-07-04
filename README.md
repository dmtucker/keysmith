# keysmith-py
Key Generator

Keysmith randomly chooses words from a list and concatenates them.
With a sufficiently large list, these make [decent passphrases](//xkcd.com/936) that tend to be more memorable than other random password generators.
The concept is essentially the same as (and arguably simpler than) [Diceware](//en.wikipedia.org/wiki/Diceware).

```
$ keysmith.py --help
usage: keysmith.py [-h] [-d DEGREE] [-q QUANTITY] [-w WORDS]

optional arguments:
  -h, --help            show this help message and exit
  -d DEGREE, --degree DEGREE
                        Specify the number of words to include.
  -q QUANTITY, --quantity QUANTITY
                        Specify the number of keys to generate.
  -w WORDS, --words WORDS
                        Specify the word list to use.
$ keysmith.py 
tillableroadsemidarkness
```

#### Pro Tip
> Use Keysmith with KeePass and Yubikey!
