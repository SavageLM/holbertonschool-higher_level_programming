#!/usr/bin/python3
# 7-add_item.py
# Logan Savage <6667@holbertonstudents.com>
"""Adds all arguments to a list and saves as a JSON str to file"""
import sys
import json

if __name__ == "__main__":
    save_json = __import__('5-save_to_json_file').save_to_json_file
    load_json = __import__('6-load_from_json_file').load_from_json_file

try:
    new_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    new_list = []
new_list.extend(sys.argv[1:])
save_jason(new_list, "add_item.json")
