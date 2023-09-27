#!/usr/bin/python3
# 11-student.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a class of Student"""


class Student:
    """A class of Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes new object Student

        Args:
            first_name (str): First name of student
            last_name (str): Last name of Student
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of a student

        If attrs is a list of strings, only attributes will be included

        Args:
            attrs (list): Attributes to include
        """
        if (type(attrs) is list and
                all(type(ele) == str for ele in attrs)):
            return {idx: getattr(self, idx)
                    for idx in attrs if hasattr(self, idx)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student instance

        Args:
            json (dict): dictionary to use
        """
        for key, value in json.items():
            setattr(self, key, value)
