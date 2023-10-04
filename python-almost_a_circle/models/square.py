#!/usr/bin/python3
# rectangle.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square.

        Args:
            size (int): Size of the Square
            x (int): x position of Rectangle.
            y (int): y position of Rectangle.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Function that assigns arguements to attributes

          Args:
            *args (ints): New attribute values.
                - 1st argument is id attribute
                - 2nd argument is size attribute
                - 3rd argument is x attribute
                - 4th argument is y attribute
        """
        if args and len(args) > 0:
            arg_num = 0
            for arguments in args:
                if arguments is None:
                    self.__init__(self.size, self.x, self.y)
                elif arg_num == 0:
                    self.id = arg_num
                elif arg_num == 1:
                    self.size = arg_num
                elif arg_num == 2:
                    self.x = arg_num
                elif arg_num == 3:
                    self.y = arg_num
                arg_num += 1
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.item():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Returns a dictionary representation of Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """Returns a printable Rectangle"""
        _class = self.__class__.__name__
        _id = self.id
        _x = self.x
        _y = self.y
        _wide = self.width
        return "[{}] ({}) {}/{} - {}".format(_class, _id, _x,
                                             _y, _wide)
