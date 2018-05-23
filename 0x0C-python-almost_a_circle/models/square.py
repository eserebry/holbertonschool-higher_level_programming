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

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute
        Args:
            args (int): set of arguments to update
            kwargs (dict): set of arguments to update
        """
        if (args is not 0 and len(args) > 0):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "size":
                    self.width = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """ returns dictionary representation of the square"""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
