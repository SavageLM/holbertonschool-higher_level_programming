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
        self.size = size
        self.position = position

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
        errmess = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(errmess)
        elif type(value[0]) is not int:
            raise TypeError(errmess)
        elif type(value[1]) is not int:
            raise TypeError(errmess)
        elif any(num < 0 for num in value):
            raise TypeError(errmess)
        self.__position = value

    def area(self):
        """Public method for getting the Area of Square"""
        return self.__size ** 2

    def my_print(self):
        """Public method that prints the Square"""
        if self.__size == 0:
            print()
        for y in range(0, self.__position[1]):
            if self.__position[1] == 0:
                continue
            else:
                print()
        for row in range(self.__size):
            for x in range(self.__position[0], 0, -1):
                print(" ", end='')
            for colomn in range(self.__size):
                print("#", end='')
            print()
