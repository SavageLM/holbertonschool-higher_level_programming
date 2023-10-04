#!/usr/bin/python3
# base.py
# Logan Savage <6667@holbertonstudents.com>
""" Declares a new base class """


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

    @staticmethod
    def from_json_string(json_string):
        """Function for converting a json string into a list"""
        if json_string is None or len(json_string) is 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of class with all attributes"""
        if dictionary is True and len(dictionary) is not 0:
            if cls.__name__ == "Rectangle":
                new_inst = cls(1, 1)
            else:
                new_inst = cls(1)
            new_inst.update(**dictionary)
            return new_inst

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that saves a JSON string to a file"""
        name = cls.__name__ + ".json"
        with open(name, "w") as newfi:
            if len(list_objs) is 0 or list_objs is None:
                newfi.write("[]")
            else:
                list_dictionaries = [ob.to_dictionary() for ob in list_objs]
                newfi.write(Base.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """Returns a JSON string converted into a list of instances"""
        name = cls.__name__ + ".json"
        try:
            with open(name, "r") as newfi:
                list_dictionaries = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in list_dictionaries]
        except IOError:
            return []
