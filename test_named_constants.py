from named_constants import Constants

class MyConstants(Constants):
    pi = 3.141592653589793
    e = 2.718281828459045
    answer = 42
    BOILERPLATE = "This code comes with no warranty."
    EURO_SYMBOL = u'\u20ac'

class Colors(Constants):
    red, yellow, green, blue, white = range(5)


class FigConstants(Constants):
    @classmethod
    def read(cls, i):
        return cls(int(i))

    def other(self):
        return "test method"


class ObjectType(FigConstants):
    CustomColor   = 0
    Ellipse       = 1
    Polygon       = 2
    Spline        = 3
    Text          = 4
    Arc           = 5
    CompoundBegin = 6
    CompoundEnd   = -6


import doctest

def test_README():
    failure_count, test_count = doctest.testfile('README.rst', verbose = True)
    assert test_count > 0
    assert failure_count == 0

def test_Colors():
    assert Colors.green == 2

def test_ObjectType():
    assert 'read' not in ObjectType
    assert 'other' not in ObjectType
