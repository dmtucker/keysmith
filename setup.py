#!/usr/bin/env python
# coding: utf-8

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import keysmith

with open('README.rst') as readme_file:
    README = readme_file.read()

setup(
    name='keysmith',
    version=keysmith.__version__,
    description=keysmith.__doc__,
    long_description=README,
    author='David Tucker',
    author_email='david.michael.tucker@gmail.com',
    license='LGPLv2+',
    url='https://github.com/dmtucker/keysmith',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    entry_points={'console_scripts': ['keysmith = keysmith.__main__:main']},
    keywords='password generator keygen',
    classifiers=[
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Intended Audience :: End Users/Desktop',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
    ],
)
