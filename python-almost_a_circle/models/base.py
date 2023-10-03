#!/usr/bin/python3
# base.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a class, Base"""


class Base:
    """Defines a class of Base"""
    __nb_objects = 0

    def __init__(self, id=none):
        """Initializes the class
        Args:
            id (int): id assigned to base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
