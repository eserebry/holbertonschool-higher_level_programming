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

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation
        Args:
            json_string (str): string representing a list of dictionaries
        """
        new_string = []
        if json_string is None or len(json_string) is 0:
            return new_string
        else:
            for i in range(len(json_string)):
                new_string = json.loads(json_string)
            return new_string

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        Args:
            cls (class): class
            dictionary (dict): a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 5)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy
