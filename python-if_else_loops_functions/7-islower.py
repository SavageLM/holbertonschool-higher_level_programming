#!/usr/bin/python3
def islower(c):

    character = ord(c)
    if 96 < character and character < 123:
        return True
    else:
        return False
