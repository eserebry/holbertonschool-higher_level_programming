#!/usr/bin/python3
class Student:
    """ defines class Student """
    def __init__(self, first_name, last_name, age):
        """ Instantiation
        Args:
            first_name(str): first_name
            last_name(str): last_name
            age(int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        return self.__dict__
