#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if len(key) == 0:
        return a_dictionary
    if key in a_dictionary:
        del a_dictionary[key]
        return a_dictionary
    return a_dictionary
