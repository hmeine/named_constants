#!/usr/bin/env python
from setuptools import setup

setup(name = 'named_constants',
      version = '1.0',
      description = ('This module offers an easy way to define named constants in Python, '
                     'supporting some simple enum-like use case, as well as arbitrary value '
                     'types like strings or floats.'),
      long_description = '''This module offers an easy way to define named constants in Python,
supporting some simple enum-like use case, as well as arbitrary value
types like strings or floats.  It is rather simple to use and does not
have a big footprint, but supports the following features:

* Ease of use (a simple class for scoping, plain definitions inside)
* Enumeration of defined constants
* Values know their *name*, i.e. you don't have to guess which meaning
  the constant value 3 has (e.g. it's name() will be 'blue' and its
  __repr__ will format as 'Colors.blue')
* Arbitrary value types (not just integers)
* Constant-ness (no change after time of definition)''',
      license = 'Apache 2.0',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2'
      ],
      author = 'Hans Meine',
      author_email = 'hans_meine@gmx.net',
      url = 'https://github.com/hmeine/named_constants',
      py_modules = ['named_constants'],
    )
