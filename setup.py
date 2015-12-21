# coding: utf-8

from __future__ import absolute_import

import setuptools

from keysmith import __version__

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='keysmith',
    version=__version__,
    license='GPL',
    description='Diceware-style Password Generator',
    long_description=long_description,
    url='https://github.com/dmtucker/keysmith-py',
    packages=['keysmith'],
    package_data={'keysmith': ['words.txt']},
    entry_points={'console_scripts': ['keysmith = keysmith.__main__:main']}
)
