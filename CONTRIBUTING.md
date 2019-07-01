# Contributing Guidelines

[GitHub](https://github.com/) hosts the project.

[![GitHub repo size](https://img.shields.io/github/repo-size/dmtucker/keysmith.svg)](https://github.com/dmtucker/keysmith)

## Development

Discuss changes by [creating an issue](https://help.github.com/articles/creating-an-issue).

[![GitHub issues](https://img.shields.io/github/issues/dmtucker/keysmith.svg)](https://github.com/dmtucker/keysmith/issues)

### Version Control

Use [`git`](https://git-scm.com/doc) to retrieve and manage the project source code.

``` sh
git clone https://github.com/dmtucker/keysmith.git
```

### Test Environment

Use [`tox`](https://tox.readthedocs.io/) to deploy and run the project source code.

``` sh
tox                                 # Build and test the project
tox -e py39                         # in a specific environment
tox -e py39 -- --pdb                # with extra options or
tox -e py39-dev -- keysmith --help  # using an arbitrary command.
```

## Merges

Propose changes by [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

[![GitHub pull requests](https://img.shields.io/github/issues-pr/dmtucker/keysmith.svg)](https://github.com/dmtucker/keysmith/pulls)

- [Branch protection](https://help.github.com/articles/about-protected-branches/) enforces acceptance criteria.
- [Milestones](https://help.github.com/en/articles/about-milestones) serve as a changelog for the project.
- [Labels](https://help.github.com/en/articles/about-labels) track the intent of each change.

### Continuous Integration

[Travis CI](https://travis-ci.com/) builds, tests, and deploys the project automatically.

[![Travis (.com) branch](https://img.shields.io/travis/com/dmtucker/keysmith/master.svg)](https://travis-ci.com/dmtucker/keysmith)

## Releases

Distribute changes by [creating a release](https://help.github.com/en/articles/creating-releases).

[![GitHub release](https://img.shields.io/github/release/dmtucker/keysmith.svg)](https://github.com/dmtucker/keysmith/releases)

1. [Change the version.](http://semver.org/)
2. [Create a tag.](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
3. [Release the tag.](https://help.github.com/en/articles/creating-releases)

### Package Repository

[PyPI](http://pypi.org/) distributes releases.

[![PyPI](https://img.shields.io/pypi/v/keysmith.svg)](https://pypi.org/project/keysmith)
