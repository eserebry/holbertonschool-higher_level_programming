class Node:
    def __init__(self, data, next_node=None):
        if isinstance(data, int) is False:
            raise TypeError("data must be an integer")
        if next_node is not None or not Node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__node = node

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            if isinstance(value, int) is False:
                raise TypeError("data must be an integer")
            else:
                self.__data = value

        @property
        def next_node(self):
            return self.__data

        @next_node.setter
        def next_node(self, value):
            if next_node(value) is not None or not Node:
                raise TypeError("next_node must be a Node object")
            else:
                self.__next_node = value


class SinglyLinkedList:
    def __init__(self):

        def sorted_insert(self, value):
