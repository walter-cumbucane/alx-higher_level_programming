#!/usr/bin/python3

def best_score(a_dictionary):
    largest = None
    key_name = None
    if not a_dictionary:
        return key_name
    for key in a_dictionary:
        if largest is None or a_dictionary[key] > largest:
            largest = a_dictionary[key]
            key_name = key
    return key_name
