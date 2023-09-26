#!/usr/bin/python3
# 8-rectangle.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a class, Rectanlge, using BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
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

        def area(self):
            """Returns the area of Rectangle"""
            return self.__width * self.__height

        def __repr__(self):
            """Returns Rectangle as a string"""
            get_class = self.__class__
            get_wide = self.__width
            get_high = self.__height
            return "[{}] {}/{}".format(get_class, get_wide, get_high)

        def __str__(self):
            """Returns a printable Rectangle"""
            rect_str = "[" + str(self.__class__)
            rect_str += "] " + str(self.__width)
            rect_str += "/" + str(self.__height)
            return rect_str
