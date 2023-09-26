#!/usr/bin/python3
# 3-is_kind_of_class.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a function that finds if obj is of class or inherited from class"""


def is_kind_of_class(obj, a_class):
    """ Function for finding if obj is class or inherited from class.

    Args:
        obj (any): object to determine.
        a_class (any): class to compare to.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
