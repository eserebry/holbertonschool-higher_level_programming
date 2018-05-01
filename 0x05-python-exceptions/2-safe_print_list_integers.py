#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real = 0
    my_int_list = [x for x in my_list if isinstance(x, int)]
    for i in my_int_list:
        try:
            if i <= x:
                print("{:d}".format(i), end="")
                real += 1
        except (IndexError, TypeError):
            return None
    print(end="\n")
    return real
