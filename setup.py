#!/usr/bin/env python3
# coding: utf-8

"""Keysmith Packaging"""

import setuptools

import keysmith


with open('README.rst') as readme_file:
    README = readme_file.read()

setuptools.setup(
    name=keysmith.__name__,
    version=keysmith.__version__,
    description=keysmith.__doc__,
    long_description=README,
    author='David Tucker',
    author_email='david@tucker.name',
    license='LGPLv2+',
    url='https://github.com/dmtucker/keysmith',
    py_modules=[keysmith.__name__],
    include_package_data=True,
    entry_points={
        'console_scripts': ['{0} = {1}:main'.format(keysmith.CONSOLE_SCRIPT, keysmith.__name__)],
    },
    keywords='password generator keygen',
    classifiers=[
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 5 - Production/Stable',
    ],
)
