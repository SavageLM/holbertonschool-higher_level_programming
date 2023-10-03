#!/usr/bin/python3
# rectangle.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a class Square that inherits from Rectangle"""
from modeles.rectangle import Rectangle


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

    def __str__(self):
        """Returns a printable Rectangle"""
        _class = self.__class__.__name__
        _id = self.id
        _x = self.x
        _y = self.y
        _wide = self.width
        return "[{}] ({}) {}/{} - {}".format(_class, _id, _x,
                                              _y, _wide)
