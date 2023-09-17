#!/usr/bin/python3

def best_score(a_dictionary):
    largest = None
    if not a_dictionary:
        return largest
    for key in a_dictionary:
        if largest is None or a_dictionary[key] > largest:
            largest = a_dictionary[key]
    return largest
