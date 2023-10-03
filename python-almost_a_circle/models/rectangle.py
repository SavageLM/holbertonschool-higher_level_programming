#!/usr/bin/python3
# rectangle.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a class Rectangle that inherits from Base"""


class Rectangle(Base):
    """ Defines a new class of Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectanbgle:

        Args:
            width (int): width of object.
            height (int): Height of object.
            x (int): x position of Rectangle.
            y (int): y position of Rectangle.
        """
        super().id.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area of the object"""
        return self.width * self.height

    def display(self):
        """Function to print a rectangle"""
        if self.width == 0 or self.height == 0:
            print()
            return
        for high in range(height):
            for wide in range(width):
                print("#", end='')
