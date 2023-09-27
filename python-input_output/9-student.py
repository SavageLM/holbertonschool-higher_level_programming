#!/usr/bin/python3
# 9-student.py
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

    def to_json(self):
        """Returns dictionary representation of a studnet"""
        return self.__dict__
