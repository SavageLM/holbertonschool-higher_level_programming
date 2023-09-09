#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if isinstance(my_list, list):
        copy = my_list.copy()
        if idx < 0:
            return my_list
        elif idx >= len(my_list):
            return my_list
        else:
            copy[idx] = element
            return copy
