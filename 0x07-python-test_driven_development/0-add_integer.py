#!/usr/bin/python3
"""

    My calculation module

"""


def add_integer(a, b=98):
    """
        Addition function
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a + b)
