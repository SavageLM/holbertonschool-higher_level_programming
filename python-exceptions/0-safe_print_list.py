#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    printed = 0
    for i in range(x):
        try:
            print("{}".format(my_string[i]), end='')
            printed += 1
        except Exception:
            pass
    return printed
