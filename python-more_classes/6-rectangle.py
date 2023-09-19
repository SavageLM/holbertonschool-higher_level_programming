#!/usr/bin/python3
# 6-rectangle.py
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

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ Returns a printable Rectangle"""
        new_rec = []
        if self.__height == 0 or self.__width == 0:
            return ("")
        for high in range(self.__height):
            for wide in range(self.__width):
                new_rec.append('#')
            if high != self.__height - 1:
                new_rec.append("\n")
        return ("".join(new_rec))

    def __repr__(self):
        """Returns a string representing a rectangle"""
        str_rec = "Rectangle(" + str(self.__width)
        str_rec += ", " + str(self.__height) + ")"
        return str_rec

    def __del__(self):
        """Detects if a rectangle has been deleted and prints a string"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
