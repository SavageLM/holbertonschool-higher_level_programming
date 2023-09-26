#!/usr/bin/python3
# 2-is_same_class.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a Function that determines if object is exact instance of class"""


def is_same_class(obj, a_class):
    """ Determines if obj is exactly class a_class

    Args:
        obj (any): object to check
        a_class (any): class to compare to
    """
    if type(obj) is a_class:
        return True
    else:
        return False
