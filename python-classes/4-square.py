#!/usr/bin/python3
# 4-square.py
# Logan Savage <6667@holbertonstudents.com>
"""Define a class- Square"""


class Square:
    """A Square with a size"""

    def __init__(self, size=0):
        """Initializes a new Square with size

        Args:
            size(int): Size of the square.
        """
        self.__size = size
    @property
    def size(self):
        """This retrieves the value of size"""
        return self.__size
    @size.setter
    def size(self, value):
        """This sets the value of size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public method for getting the Area of Square"""
        return self.__size ** 2
