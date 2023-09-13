#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    uniques = set()
    if set_1 is None:
        return set_2
    if set_2 is None:
        return set_1
    if set_1 is None and set_2 is None:
        return 0
    for i in set_1:
        if i not in set_2:
            uniques.add(i)
    for i in set_2:
        if i not in set_1:
            uniques.add(i)
    return uniques
