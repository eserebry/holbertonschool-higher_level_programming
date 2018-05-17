#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """  writes an Object to a text file, using a JSON representation
    Args:
        my_obj: an objext to write
        filename(str): text file to write to
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
