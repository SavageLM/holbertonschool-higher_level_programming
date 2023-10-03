#!/usr/bin/python3
# base.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a class, Base"""


class Base():
    """Defines a class of Base"""
    __nb_objects = 0

    def __init__(self, id=none):
        """Initializes the class"""
        if id is not None:
            self.id = None
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
