"""Package Keysmith."""


import codecs
import os.path

import setuptools  # type: ignore

import keysmith  # This project only depends on the standard library.


def read(*parts):
    """Read a file in this repository."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), 'r') as file_:
        return file_.read()


ENTRY_POINTS = {
    'console_scripts': [
        '{name}={module}:{function}'.format(
            name=keysmith.CONSOLE_SCRIPT,
            module=keysmith.__name__,
            function=keysmith.main.__name__,
        ),
    ],
}


if __name__ == '__main__':
    setuptools.setup(
        name=keysmith.__name__,
        version=keysmith.__version__,
        description='Passphrase Generator',
        long_description=read('README.rst'),
        author='David Tucker',
        author_email='david@tucker.name',
        license='BSD 3-Clause License',
        url='https://github.com/dmtucker/keysmith',
        python_requires='~=3.5',
        py_modules=[keysmith.__name__],
        entry_points=ENTRY_POINTS,
        keywords='diceware generator keygen passphrase password',
        classifiers=['Development Status :: 7 - Inactive'],
    )
