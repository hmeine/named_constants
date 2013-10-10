
USAGE
====

This module is used by deriving from ``constants.Constants`` in order
to define constants in a common namespace::

   >>> import constants
   >>> class MyConstants(constants.Constants):
   ...     pi = 3.141592653589793
   ...     e = 2.718281828459045
   ...
   >>> print(MyConstants.pi / 2)
   1.5707963267948966

As you can see, the named constants behave as expected, since they are
instances of subclasses of the original type.  The only special feature
about them is their string representation, and that they have a name()::

  >>> MyConstants.pi
  MyConstants.pi
  >>> print(MyConstants.pi)
  3.141592653589793
  >>> type(MyConstants.pi)
  <class 'constants.NamedFloat'>
  >>> assert isinstance(MyConstants.pi, float)
  >>> MyConstants.pi.name()
  'pi'

One common use case will be the definition of some enum-like identifiers::

  >>> class Colors(constants.Constants):
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

The namespaces also allow some dict-like introspection::

  >>> len(Colors)
  5
  >>> assert Colors.values() == list(range(5)) == list(Colors)
  >>> Colors.has_key('blue')
  True
  >>> Colors.has_key('purple')
  False
  >>> for key, value in Colors.iteritems():
  ...     print("%10s: %s" % (key, value))
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
