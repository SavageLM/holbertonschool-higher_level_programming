#!/usr/bin/python3
# 2-square.py
# Logan Savage <6667@holbertonstudents.com>
"""Define a class- Square"""


class Square:
    """A Square with a size"""

    def __init__(self, size=0):
        """Initializes a new Square with size

        Args:
            size(int): Size of the square.
        """
        if type(size) is not int:
            """Evaluates if size is an int"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """Evalutes tif size is a positive integer"""
            raise ValueError("size must be >= 0")
        self.__size = size
