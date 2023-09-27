#!/usr/bin/python3
# 6-load_from_json_file.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a function  that loads a JSON str from file"""
import json


def load_from_json_file(filename):
    """Function that loads a JSON str from a file.

    Args:
        filename (file): file to load from.
    """
    with open(filename, "r", encoding="utf-8") as newfi:
        return json.load(newfi)
