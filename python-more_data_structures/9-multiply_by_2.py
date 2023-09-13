#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    if a_dictionary is None:
        return None
    new_dict = {}
    double_val = 0
    for key in a_dictionary:
        value = a_dictionary.get(key)
        double_val = value * 2
        new_dict.update({key: double_val})
    return new_dict
