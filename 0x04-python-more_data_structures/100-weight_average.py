#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not 0:
        top = 0
        bottom = 0
        result = 0
        for i in my_list:
            top += i[0] * i[1]
            bottom += i[1]
        result = top / bottom
        return result
    return 0
