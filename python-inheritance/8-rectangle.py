#!/usr/bin/python3
# 8-rectangle.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a class, Rectanlge, using BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectanlge(BaseGeometry):
    """A class Rectangle that inherits BaseGeometry"""

    def __init__(self, width, height):
        """ Initializes an object of class Rectangle.

        Args:
            width (int): width of the object.
            height (int): height of the object.
        Validates width and height with integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
