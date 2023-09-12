#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) > 0:
        a = tuple_a[0]
    else:
        a = 0
    if len(tuple_a) > 1:
        c = tuple_a[1]
    else:
        c = 0
    if len(tuple_b) > 0:
        b = tuple_b[0]
    else:
        b = 0
    if len(tuple_b) > 1:
        d = tuple_b[1]
    else:
        d = 0
    new_tup = (a + b, c + d)
    return new_tup
