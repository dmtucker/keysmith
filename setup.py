# coding: utf-8

from __future__ import absolute_import

import setuptools

from keysmith import __version__

setuptools.setup(
    name='keysmith',
    version=__version__,
    license='GPL',
    description='Diceware-style Password Generator',
    url='https://github.com/dmtucker/keysmith-py',
    packages=['keysmith'],
    package_data={'keysmith': ['words.txt']},
    entry_points={'console_scripts': ['keysmith = keysmith.__main__:main']}
)
