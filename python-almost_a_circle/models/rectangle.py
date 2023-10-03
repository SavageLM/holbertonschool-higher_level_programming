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
