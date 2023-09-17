#!/usr/bin/python3

def number_keys(a_dictionary):
    result = 0
    if not a_dictionary:
        return result
    for key in a_dictionary:
        result += 1
    return result
