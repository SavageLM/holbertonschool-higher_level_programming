#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    true_list = []
    if len(my_list) == 0:
        return None
    for i in my_list:
        if abs(i) % 2 == 0:
            true_list.append(True)
        else:
            true_list.append(False)
    return true_list
