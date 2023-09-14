#!/bin/usr/python3
# 1-square.py
"""Define a class- Square"""

class Square:
    """A Square with a size"""
    def __int__(self, size):
        """Initializes a new Square with size
        Args:
            size(int): Size of the square.
        """
        self.__size = size
