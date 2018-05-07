#!/usr/bin/python3
class Rectangle:
    """ class defines rectangle """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __str__(self):
        my_rect = ""
        if self.__height == 0 or self.__width == 0:
            return "\n"
        for i in range(self.__height):
            for k in range(self.__width):
                my_rect += "#"
            if (i < self.__height - 1):
                my_rect += "\n"
        return my_rect
