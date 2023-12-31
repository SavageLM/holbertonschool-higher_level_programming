#!/usr/bin/python3
# 0-add_integer.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a function that adds to ints or floats"""


def add_integer(a, b=98):
    """Returns sum of a and b.

    Floats will be cast to int.

    Exceptions:
        raises TypeError if a or b are not int or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
