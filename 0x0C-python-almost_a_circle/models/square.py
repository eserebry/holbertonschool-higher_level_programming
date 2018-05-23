#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Ititialize class Square
        Args
            width (int): widht
            height (int): height
            x (int): lenght
            y (int): height
            id (int): id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns string with the square arguments"""
        return "[Square] (%s) %s/%s - %s" % \
            (self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ returns size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """ get size
        Args:
            value (int): value
        """
        self.width = value
