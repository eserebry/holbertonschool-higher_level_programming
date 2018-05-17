#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """  returns the JSON representation of an object (string)
    Args:
        my_obj(str): string to encode
    """
    return json.dumps(my_obj)
