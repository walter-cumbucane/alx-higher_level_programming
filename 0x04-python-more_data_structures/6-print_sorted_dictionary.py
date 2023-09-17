#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = list()
    for key in a_dictionary:
        keys.append(key)
    keys.sort()
    for key in keys:
        print(f"{key}: {a_dictionary[key]}")
