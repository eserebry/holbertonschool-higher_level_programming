#!/usr/bin/python3
def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return [[]]

    new_list = []
    for i in range(1, n):
        new_list2 = []
        for j in range(i):
            new_list2.append(1)
        new_list.append(new_list2)
    return new_list
