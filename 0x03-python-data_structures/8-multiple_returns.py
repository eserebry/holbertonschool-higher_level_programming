#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        char = None
        lenght = 0
        return lenght, char
    lenght = len(sentence)
    char = sentence[0]
    return lenght, char
