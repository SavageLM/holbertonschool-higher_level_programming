#!/usr/bin/python3
# rectangle.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a class Rectangle that inherits from Base"""
from models.base import Base


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
        super().__init__(id)
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
        for y_pos in range(self.y):
                print('')
        for high in range(self.height):
            for x_pos in range(self.x):
                print(" ", end="")
            for wide in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """Returns a printable Rectangle"""
        _class = self.__class__.__name__
        _id = self.id
        _x = self.x
        _y = self.y
        _wide = self.width
        _high = self.height
        return "[{}] ({}) {}/{} - {}/{}".format(_class, _id, _x,
                                                _y, _wide, _high)

    def update(self, *args, **kwargs):
        """Function that assigns arguements to attributes

          Args:
            *args (ints): New attribute values.
                - 1st argument is id attribute
                - 2nd argument is width attribute
                - 3rd argument is height attribute
                - 4th argument is x attribute
                - 5th argument is y attribute
        """
        if args and len(args) > 0:
            arg_num = 0
            for arguments in args:
                if arguments is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                elif arg_num == 0:
                    self.id = arguments
                elif arg_num == 1:
                    self.width = arguments
                elif arg_num == 2:
                    self.height = arguments
                elif arg_num == 3:
                    self.x = arguments
                elif arg_num == 4:
                    self.y = arguments
                arg_num += 1
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary of Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
