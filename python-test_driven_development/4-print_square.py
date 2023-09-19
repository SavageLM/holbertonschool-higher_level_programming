#!/usr/bin/python3
# 4-print_square.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a function that prints a square """


def print_square(size):
    """Prints a square of size

    Raises:
    TypeError if size is not an int
    ValueError if size is not positive
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end='')
            print()
