#!/usr/bin/python3
# 3-to_json_string.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a function that returns an object as a JSON str"""
import json


def to_json_string(my_obj):
    """Function that returns an object as a JSON str.

    Args:
        my-obj (any): object to turn into JSON str.
    """
    return json.dumps(my_obj)
