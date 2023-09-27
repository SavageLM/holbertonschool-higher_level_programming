#!/usr/bin/python3
# 8-class_to_json.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines a function that converts class to JSON"""


def class_to_json(obj):
    """Returns dictionary description of a simple structure"""
    return obj.__dict__
