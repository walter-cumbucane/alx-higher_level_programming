#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for key, valuee in sorted(a_dictionary.items()):
        if valuee == value:
            del a_dictionary[key]
    return a_dictionary
