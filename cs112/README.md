> At this point, _only [the Python implementation](//github.com/dmtucker/keysmith-py) should be used_ because of the way the other implementations generate random numbers (via HTTPS).
  The [C](//github.com/dmtucker/keysmith-c), [Haskell](//github.com/dmtucker/keysmith-hs), and [Java](//github.com/dmtucker/keysmith-java) implementations were done as part of [a project for a comparative programming class](//github.com/dmtucker/cs112) I took in college when having more points of comparison (namely, network-related requirements) was more useful than having a secure key generator.
  Keysmith has since become more useful to me as the latter, so I wrote [keysmith-py](//github.com/dmtucker/keysmith-py) which uses Python's `random.SystemRandom()` method making it lighter, faster, (better, harder, stronger,) and more secure.


keysmith
========

Key Generator

# SYNOPSIS
```
keysmith [-h] [-v] [-V] [length]
```

# DESCRIPTION

keysmith uses a random number generator to select `[length]` number of "teeth" (words) from a list (see `DEFAULT_WORDS` below) and generates a key by concatenating them.

> All implementations currently use the RANDOM.ORG generator over HTTP.
  They use the cURL library and require a network connnection.

The following options are available:
```
-d      Print details about the generated token (teeth and length).
          Note: Details are currently only available in the C Implementation.
  
-h      Show help
  
-v      Print verbose output.
  
-V      Print version
```

# CONSTANTS

* `DEFAULT_DEGREE`
  number of teeth to put in the key if unspecified, default: 3
    
* `DEFAULT_WORDS`  - location of the word list to draw teeth from, default: etc/word.list
  Note: The word list must have UNIX-style line endings ('\n').

# EXAMPLES
```
$ keysmith 4
> correcthorsebatterystaple
  |_____||___||_____||____|
     1     2     3     4    <- teeth of the generated 4th-degree key
```
