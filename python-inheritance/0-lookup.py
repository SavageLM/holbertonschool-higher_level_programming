#!/usr/bin/python3
# 0-lookup.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a function that gets all attributes and methods of an object"""


def lookup(obj):
    """Returns a list of attributes and methods of obj

    Args:
        obj (any): object to retirieve from
    """
    return list(dir(obj))
