#!/usr/bin/python3
def write_file(filename="", text=""):
    """  writes a string to a text file (UTF8)
    and returns the number of characters written:
    Args:
        filename(str): filename
        text(str): text to be written
    """
    num = 0
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
