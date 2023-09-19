#!/usr/bin/python3
# 1-rectangle.py
# Logan Savage <6667@holbertonstudents.com>
"""Define a class- Rectangle"""


class Rectangle:
    """This is a class for making a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle.

        Args:
            self: The rectangle
            width (int): width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle.

        Args:
            self: The rectangle
            value (int): value width will be set to
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle.

        Args:
            self: The rectangle
            value (int): value width will be set to
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
