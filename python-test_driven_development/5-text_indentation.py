#!/usr/bin/python3
# 5-text_indentation.py
# Logan Savage <6667@holbertonstudents.com>
""" Defines a function that prints a text """


def text_indentation(text):
    """Prints a text

    Raises:
    TypeError if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    sentence = ""
    for i in range(len(text)):
        if text[i] is not "." and text[i] is not "?" and text[i] is not ":":
            sentence += text[i]
        else:
            sentence += text[i]
            print(sentence)
            print()
            sentence = ""
            while i < (len(text) -1) and text[i + 1] == " ":
                i += 1
    print(sentence, end='')
