#!/usr/bin/python3
def uppercase(str):

    for i in str:
        character = ord(i)
        if 96 < character and character < 123:
            character = character - 32
            print("{:c}".format(character), end='')
        else:
            print("{:c}".format(character), end='')
