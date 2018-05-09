#!/usr/bin/python3
class Rectangle:
    """ class defines rectangle """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
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

    def __repr__(self):
        return "Rectangle(%s, %s)" % (self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
