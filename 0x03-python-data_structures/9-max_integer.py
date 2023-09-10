#!/usr/bin/python

def max_integer(my_list=[]):
    if not my_list:
        return None
    maximum = None
    for num in my_list:
        if maximum is None or num > maximum:
            maximum = num
    return maximum
