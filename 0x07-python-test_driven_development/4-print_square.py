#!/usr/bin/python3
"""
    My calculation module

"""


def print_square(size):
    """
        Function that prints a square with the character #.

    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
