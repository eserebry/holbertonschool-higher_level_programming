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
    text = text.replace(". ", ".\n\n")
    text = text.replace(": ", ":\n\n")
    text = text.replace("? ", "?\n\n")
    print("\n".join(i.lstrip() for i in text.split("\n")), end="")
