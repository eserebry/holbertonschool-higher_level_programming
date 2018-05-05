#!/usr/bin/python3
def text_indentation(text):
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
