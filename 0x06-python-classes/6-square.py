#!/usr/bin/python3
class Square:
    """modul that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if isinstance(position, tuple) is False or len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) is False or\
           isinstance(position[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if isinstance(value, tuple) is False or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) is False or\
           isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
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
