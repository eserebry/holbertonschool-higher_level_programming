#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8) and prints it to stdout
    Args:
        filename(str): filename
        nb_lines(int): number of lines
    """
    num = 0
    with open(filename, encoding="utf-8") as myFile:
        if nb_lines <= 0:
            print(myFile.read(), end="")
        for line in range(nb_lines):
            print(myFile.readline(), end="")
