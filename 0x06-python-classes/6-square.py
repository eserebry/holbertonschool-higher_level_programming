#!/usr/bin/python3
class Square:
    """modul that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is not True and len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False\
           and isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        area = self.__size ** 2
        return (area)

    def my_print(self):
        if self.__size == 0:
            print()
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for l in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
