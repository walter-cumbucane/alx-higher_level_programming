#!/usr/bin/python3

def no_c(my_string):
    if no my_string:
        return None
    new_string = ""
    for char in my_string:
        if char == "c":
            continue
        new_string += char
    return new_string
