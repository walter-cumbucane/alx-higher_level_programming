#!/usr/bin/python3

def no_c(my_string):
    no_cs = []
    delimeter = ""
    for char in my_string:
        if char == "c":
            continue
        no_cs.append(char)
    new_string = delimeter.join(no_cs)
