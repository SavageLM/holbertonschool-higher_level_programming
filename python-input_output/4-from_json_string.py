#!/usr/bin/python3
# 4-from_json_string.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a function that returns an JSON str as an object"""
import json


def from_json_string(my_str):
    """Function that returns a JSON str as an Obj.

    Args:
        my_str (str): JSON str to turn into object.
    """
    return json.loads(my_str)
