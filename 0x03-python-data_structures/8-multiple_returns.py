#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    lenght = len(sentence)
    char = sentence[0]
    return lenght, char
