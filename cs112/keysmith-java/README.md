keysmith-java
=============
Key Generator

> At this point, _only [the Python implementation](//github.com/dmtucker/keysmith-py) should be used_ because of the way the other implementations generate random numbers (via HTTPS).
  The [C](//github.com/dmtucker/keysmith-c), [Haskell](//github.com/dmtucker/keysmith-hs), and [Java](//github.com/dmtucker/keysmith-java) implementations were done as part of [a project for a comparative programming class](//github.com/dmtucker/cs112) I took in college when having more points of comparison (namely, network-related requirements) was more useful than having a secure key generator.
  Keysmith has since become more useful to me as the latter, so I wrote [keysmith-py](//github.com/dmtucker/keysmith-py) which uses Python's `random.SystemRandom()` method making it lighter, faster, (better, harder, stronger,) and more secure.
