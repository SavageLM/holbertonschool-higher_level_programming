#!/usr/bin/python3
# 2-matrix_divided.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a function that prints a name """


def say_my_name(first_name, last_name=""):
    """Prints a name

    Raises:
    TypeError if first/last name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
