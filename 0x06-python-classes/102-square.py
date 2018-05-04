#!/usr/bin/python3
class Square:
    """modul that defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)) is not True:
            raise TypeError("size must be a number")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        return self.__size < other.__size
    def __le__(self, other):
        return self.__size <= other.__size
    def __eq__(self, other):
        return self.__size == other.__size
    def __ne__(self, other):
        return self.__size != other.__size
    def __gt__(self, other):
        return self.__size > other.__size
    def __ge__(self, other):
        return self.__size >= other.__size
