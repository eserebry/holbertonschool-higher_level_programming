#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
    total = 0
    if roman_string is not None:
        prev = 1001
        for key in roman_string:
            if dict[key] > prev:
                total += dict[key] - (prev*2)
            else:
                total += dict[key]
                prev = dict[key]
        return total
    return 0
