#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_list = set()
    result = 0
    for element in my_list:
        unique_list.add(element)
    for element in unique_list:
        result += element
    return result
