#!/usr/bin/python3
# 0-read_file.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """Function to read a file.

    Args:
        filename (file): File to be read.
    """
    if filename is not "":
        with open(filename, encoding="utf-8") as newfi:
            print(newfi.read(), end="")
