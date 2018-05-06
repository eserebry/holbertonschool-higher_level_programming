#!/usr/bin/python3
"""
    My calculation module

"""


def say_my_name(first_name, last_name=""):
    """
        Function that prints a square with the character #.

    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}" .format(first_name, last_name))
