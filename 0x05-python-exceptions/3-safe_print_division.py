#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0.0
    try:
        c = a / b
    except (ZeroDivisionError):
        return None
    finally:
        print("Inside result:{:0.1f}".format(c))
        return c