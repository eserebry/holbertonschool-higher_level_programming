#!/usr/bin/python3
class MyList(list):
    """ class  inherits from list """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print("{}".format(sorted(self)))
