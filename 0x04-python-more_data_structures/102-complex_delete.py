#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dict = {}
    for key in a_dictionary:
        if a_dictionary[key] == value:
            continue
        new_dict[key] = value
    return new_dict
