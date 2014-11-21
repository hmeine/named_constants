Overview
========

This module offers an easy way to define named constants in Python,
supporting some simple enum-like use case, as well as arbitrary value
types like strings or floats.  It is rather simple to use and does not
have a big footprint, but supports the following features:

* Ease of use (a simple class for scoping, plain definitions inside)
* Enumeration of defined constants
* Values know their *name*, i.e. you don't have to guess which meaning
  the constant value 3 has (e.g. it's name() will be 'blue' and its
  __repr__ will format as 'Colors.blue')
* Arbitrary value types (not just integers)
* Constant-ness (no change after time of definition)

There are unit tests, and there is a Python 3 branch available.

Usage
=====

This module is used by deriving from ``named_constants.Constants`` in
order to define constants in a common namespace::

   >>> from named_constants import Constants
   >>> class MyConstants(Constants):
   ...     pi = 3.141592653589793
   ...     e = 2.718281828459045
   ...
   >>> print MyConstants.pi / 2
   1.57079632679

As you can see, the definitions behave as expected, since they are
still instances of (subclasses of) the original type.  They do offer
some additional features, however, most notably that their string
representation reveals the constant's name, and that they also have a
corresponding name() getter function::

  >>> MyConstants.pi
  MyConstants.pi
  >>> print MyConstants.pi
  3.14159265359
  >>> type(MyConstants.pi)
  <class 'named_constants.NamedFloat'>
  >>> assert isinstance(MyConstants.pi, float)
  >>> MyConstants.pi.name()
  'pi'

One common use case will be the definition of some enum-like identifiers::

  >>> class Colors(Constants):
  ...     red, yellow, green, blue, white = range(5)
  ...
  >>> Colors.blue
  Colors.blue
  >>> Colors.black = None
  Traceback (most recent call last):
   ...
  TypeError: Constants are not supposed to be changed ex post

The named constants can also be looked up by name or by value::

  >>> Colors(3)
  Colors.blue
  >>> Colors('white') is Colors.white
  True

The singleton-like semantics allow you to use equality checks or
identity checks, depending on what shall be the result when comparing
with the original value::

  >>> color1 = 3
  >>> color2 = Colors(color1)
  >>> color3 = Colors('blue')
  >>> color1 == color2
  True
  >>> color1 is color2
  False
  >>> color2 is Colors.blue
  True
  >>> color3 is Colors.blue
  True

The namespaces also allow some dict-like introspection::

  >>> len(Colors)
  5
  >>> assert Colors.values() == range(5) == list(Colors)
  >>> Colors.has_key('blue')
  True
  >>> Colors.has_key('purple')
  False
  >>> for name in Colors.iterkeys():
  ...     print name
  red
  yellow
  green
  blue
  white
  >>> for key, value in Colors.iteritems():
  ...     print "%10s: %s" % (key, value)
         red: 0
      yellow: 1
       green: 2
        blue: 3
       white: 4

Note that iterating over the namespace (e.g. using the standard
``keys()``, ``values()``, ``items()``, their iter variants, or just ``for
constant in MyConst``), the results will be *sorted* by the values (not
the keys/names).  This is particularly useful for dumping tables like
above.

Note that ``Colors.has_key(x)`` is *not* the same as ``x in Colors``,
because the latter equals ``Colors.has_key(x) or Colors.has_value(x)``::

  >>> 3 in Colors
  True
  >>> 17 in Colors
  False
  >>> 'blue' in Colors
  True
  >>> 'silver' in Colors
  False
  >>> Colors.has_value(3)
  True
  >>> Colors.has_key('blue')
  True
  >>> Colors.has_key(3)
  False
