#!/usr/bin/python3
def islower(c):

    character = ord(c)
    if 97 < character and character < 122:
        return True
    else:
        return False
