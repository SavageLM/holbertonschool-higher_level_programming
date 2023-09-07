#!/usr/bin/python3
def uppercase(str):

    newstr = ""
    for i in str:
        character = ord(i)
        if 96 < character and character < 123:
            character = character - 32
            character = chr(character)
            newstr += character
        else:
            character = chr(character)
            newstr += character
    print("{}".format(newstr))
