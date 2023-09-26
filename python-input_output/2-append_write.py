#!/usr/bin/python3
# 2-append_write.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a function that appends text to a file"""


def append_write(filename="", text=""):
    """Function that appends text to a file.

    Args:
        filename (file): File to add to
        text (str): Text to add
    """
    with open(filename, "a", encoding="utf-8") as newfi:
        return newfi.write(text)
