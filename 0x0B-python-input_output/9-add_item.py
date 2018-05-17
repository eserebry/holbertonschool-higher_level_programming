#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """  Write a function that creates an Object from a “JSON file”
    Args:
        filename(str): text file
    """
    with open(filename, encoding="utf-8") as myFile:
        return json.load(myFile)
