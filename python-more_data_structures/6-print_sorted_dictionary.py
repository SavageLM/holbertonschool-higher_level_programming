#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    sorted_keys = sorted(a_dictionary.items(), key=lambda x: x[0])
    for key, value in sorted_keys:
        print("{:s}: {}".format(key, value))
