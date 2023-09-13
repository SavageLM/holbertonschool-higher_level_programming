#!/usr/bin/python3
def best_score(a_dictionary):

    bestest = 0
    person = ""
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    for key in a_dictionary:
        value = a_dictionary.get(key)
        if value > bestest:
            bestest = value
            person = key
    return person
