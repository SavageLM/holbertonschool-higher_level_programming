#!/usr/bin/python3
# 4-inherits_from.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a function that determines if obj is an inherited class"""


def inherits_from(obj, a_class):
    """Function to determine if obj is an inherited class.

    Args:
        obj (any): object to determine
        a_class (any): class to compare to.
    """
    if issubclas(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
