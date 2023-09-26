#!/usr/bin/python3
# 1-my_list.py
# Logan Savage <6667@holbertonstudents.com>
"""Defines an inherited list class of MyList"""


class MyList(list):
    """Implemention of a sorted print for list class"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
