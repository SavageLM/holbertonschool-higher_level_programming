#!/usr/bin/python3
# 7-base_geometry.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a class, BaseGeometry"""


class BaseGeometry:
    """A class of BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value.

        Args:
            name (str): name of value
            value (int): value to check
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
