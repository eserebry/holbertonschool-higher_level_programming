#!/usr/bin/python3
"""
    My calculation module

"""


def text_indentation(text):
    """
        Function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    """
    new_string = ""
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if ((text[i - 1] == '.' or text[i - 1] == '?' or text[i - 1] == ":")  and (i is not 0)):
            new_string += "\n\n"
        else:
            new_string += text[i]
        if (i + 1  == len(text)):
            print("{}".format(new_string), end="")
