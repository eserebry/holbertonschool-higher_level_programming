#!/usr/bin/python3
"""
    My calculation module

"""


def text_indentation(text):
    """
        Function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (text[i - 1] == "." or text[i - 1] == "?"or text[i - 1] == ":")\
           and i != 0:
            print()
            print()
        else:
            print(text[i], end="")
    print()
