#!/usr/bin/python3
def common_elements(set_1, set_2):

    commons = set()
    if set_1 is None or set_2 is None:
        return 0
    for i in set_1:
        if i in set_2:
            commons.add(i)
    return commons

