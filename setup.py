#!/usr/bin/env python3

"""Package Keysmith."""

import setuptools  # type: ignore

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
    python_requires='~=3.5',
    py_modules=[keysmith.__name__],
    entry_points={
        'console_scripts': [
            '{script_name}={module}:main'.format(
                script_name=keysmith.CONSOLE_SCRIPT,
                module=keysmith.__name__,
            ),
        ],
    },
    keywords='password generator keygen',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved'
        ' :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
