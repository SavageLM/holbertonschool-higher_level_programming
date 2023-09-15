#!/usr/bin/python3
# 6-square.py
# Logan Savage <6667@holbertonstudents.com>
"""Define a class- Square"""


class Square:
    """A Square with a size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square with size

        Args:
            size(int): Size of the square.
            position(int, int): position of square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """This retrieves the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This sets the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not int and value < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public method for getting the Area of Square"""
        return self.__size ** 2

    def my_print(self):
        """Public method that prints the Square"""
        if self.size == 0:
            print()
        for y in range(0, self.position[1]):
            print()
        for row in range(self.size):
            for colomn in range(self.size):
                for x in range(self.position[0], 0):
                    print(" ", end='')
                print("#", end='')
            print()
