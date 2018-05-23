#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """  class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Ititialize class Rectangle
        Args
            width (int): widht
            height (int): height
            x (int): lenght
            y (int): height
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns  the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ get width
        Args:
            value (int): value
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ get height
        Args:
            value (int): value
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ returns lenght"""
        return self.__x

    @x.setter
    def x(self, value):
        """ get lenght
        Args:
            value (int): value
        """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns height"""
        return self.__y

    @y.setter
    def y(self, value):
        """ get height
        Args:
            value (int): value
        """
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """ displays rectangle"""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ returns string with the rectangle arguments"""
        return "[Rectangle] (%s) %s/%s - %s/%s" % \
            (self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """ prints the Rectangle with height and lenght parameters"""
        for i in range(self.__y):
            print()
        for k in range(self.__height):
            print(" " * self.__x, end="")
            for l in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """ assigns an argument to each attribute
        Args:
            args (int): set of arguments to update
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.__width = args[i]
            if i == 2:
                self.__height = args[i]
            if i == 3:
                self.__x = args[i]
            if i == 4:
                self.__y = args[i]
