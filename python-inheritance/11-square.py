#!/usr/bin/python3
# 11-square.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a class, Square, using BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits Rectangle"""

    def __init__(self, size):
        """ Initializes an object of class Rectangle.

        Args:
            size (int): Size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
