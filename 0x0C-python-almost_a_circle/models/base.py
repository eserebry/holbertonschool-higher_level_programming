#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialising Base
        Args:
            id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): list of the dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): list of instances who inherits of Base
            cls (class): a class
        """
        myfile = cls.__name__ + ".json"
        savefile = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                savefile.append(cls.to_dictionary(list_objs[i]))
        with open(myfile, mode="w", encoding="utf-8") as new_file:
                new_file.write(cls.to_json_string(savefile))
