#!/usr/bin/python3
def number_of_lines(filename=""):
    """ returns the number of lines of a text file:
    Args:
        filename(str): filename
    """
    num = 0
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            num += 1
    return num
