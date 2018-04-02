#!/usr/bin/env python3

"""Package Keysmith."""


import codecs
import os.path
import re

import setuptools  # type: ignore


def read(*parts):
    """Read a file in this repository."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'r') as file_:
        return file_.read()


def find_version(*file_paths):
    """
    Read the file in setup.py and parse the version with a regex.

    https://packaging.python.org/guides/single-sourcing-package-version/
    """
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='keysmith',
    version=find_version('keysmith.py'),
    description='Passphrase Generator',
    long_description=read('README.rst'),
    author='David Tucker',
    author_email='david@tucker.name',
    license='LGPLv2+',
    url='https://github.com/dmtucker/keysmith',
    python_requires='~=3.5',
    py_modules=['keysmith'],
    entry_points={'console_scripts': ['keysmith=keysmith:main']},
    keywords='diceware generator keygen passphrase password',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved'
        ' :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
