#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for i in my_list:
        if (i <= x):
            print("{:d}" .format(i), end="")
            num += 1
    print(end="\n")
    return (num)
