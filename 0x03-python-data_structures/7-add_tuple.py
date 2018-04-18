#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) >= 2:
        sum_a = tuple_b[0]
        sum_b = tuple_b[1]
    if len(tuple_a) == 0 and len(tuple_b) == 1:
        sum_a = tuple_b[0]
        sum_b = 0
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        sum_a = 0
        sum_b = 0
    if len(tuple_a) == 1 and len(tuple_b) >= 2:
        sum_a = tuple_a[0]+tuple_b[0]
        sum_b = tuple_b[1]
    if len(tuple_a) == 1 and len(tuple_b) == 1:
        sum_a = tuple_a[0]+tuple_b[0]
        sum_b = 0
    if len(tuple_a) == 1 and len(tuple_b) == 0:
        sum_a = tuple_a[0]
        sum_b = 0
    if len(tuple_b) == 0 and len(tuple_a) >= 2:
        sum_a = tuple_a[0]
        sum_b = tuple_a[1]
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        sum_a = tuple_a[0]+tuple_b[0]
        sum_b = tuple_a[1]+tuple_b[1]
    if len(tuple_a) >= 2 and len(tuple_b) == 1:
        sum_a = tuple_a[0]+tuple_b[0]
        sum_b = tuple_a[1]
    return sum_a, sum_b
