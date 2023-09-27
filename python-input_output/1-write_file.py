#!/usr/bin/python3
# 1-write_file.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a function that writes a text to a file"""


def write_file(filename="", text=""):
    """Function to write a text to a file.

    Args:
        filename (file): File to be written to.
        text (str): text to write to file.
    """
    with open(filename, "w", encoding="utf-8") as newfi:
        return newfi.write(text)
