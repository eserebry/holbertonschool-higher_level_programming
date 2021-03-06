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
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        area = self.__size ** 2
        return (area)

    def my_print(self):
        if (self.__size == 0):
            print(end="\n")
        for i in range(0, self.__size):
            for k in range(0, self.__size):
                print('#', end="")
            print(end="\n")
