#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    list_tuples = list()
    for key, value in a_dictionary.items():
        list_tuples.append((key, value))
    list_tuples.sort()
    for key, value in list_tuples:
        print(f"{key}: {value}")
