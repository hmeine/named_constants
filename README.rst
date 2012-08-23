
USAGE
====

This module is used by deriving from ``constants.Constants`` in order
to define constants in a common namespace::

   >>> import constants
   >>> class MyConstants(constants.Constants):
   ...     pi = 3.141592653589793
   ...     e = 2.718281828459045
   ... 
   >>> print MyConstants.pi / 2
   1.57079632679

As you can see, the named constants behave as expected; the only
special feature about them is their string representation::

  >>> MyConstants.pi
  MyConstants.pi
  >>> print MyConstants.pi
  3.14159265359

One common use case will be the definition of some enum-like identifiers::

  >>> class Colors(constants.Constants):
  ...     red, yellow, green, blue, white = range(5)
  ... 
  >>> Colors.blue
  Colors.blue
  >>> type(Colors.blue)
  <class 'constants.Const'>
  >>> Colors.black = None
  Traceback (most recent call last):
   ...
  TypeError: Constants are not supposed to be changed ex post

The named constants can also be looked up by name or by value::

  >>> Colors(3)
  Colors.blue
  >>> Colors('white') is Colors.white
  True

The namespaces also allow some dict-like introspection::

  >>> len(Colors)
  5
