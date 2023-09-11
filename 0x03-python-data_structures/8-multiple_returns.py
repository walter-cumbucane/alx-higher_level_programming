#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        tuple_a = (0, None)
    else:
        tuple_a = (length, sentence[0])
    return tuple_a
