#!/usr/bin/python3
# 5-save_to_json_file.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a function  that saves a JSON str to file"""
import json


def save_to_json_file(my_obj, filename):
    """Function that saves a JSON str to a file.

    Args:
        my_obj (any): object to convert to JSON str and save
        filename (file): file to save to.
    """
    with open(filename, "w", encoding="utf-8") as newfi:
        json.dump(my_obj, newfi)
