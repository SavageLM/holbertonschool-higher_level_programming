#!/usr/bin/python3
# base.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a class, Base"""


class Base:
    """Defines a class of Base"""
    __nb_objects = 0

    def __init__(self, id=none):
        """Initializes the class
        Args:
            id (int): id assigned to base object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that Returns the JSON string for a list of dictionaries"""
        if len(list_dictionaries) is 0 or list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that saves a JSON string to a file"""
        name = cls.__name__ + .json
        with open(name, "w") as newfi:
            if len(list_objs) is 0 or list_objs is None:
                newfi.write("[]")
            else:
                newfi.write(Base.to_json_string(list_objs))
