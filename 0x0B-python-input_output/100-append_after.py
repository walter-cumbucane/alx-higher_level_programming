#!/usr/bin/python3
"""This module contains a function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after a each line with a string"""
    with open(filename, "r") as file:
        lines = file.readlines()
    flag = 0
    index = 0
    for line in lines:
        if flag == 1:
            part1 = lines[:insert_position]
            part2 = lines[insert_position:]
            lines = part1 + [new_string] + part2
            index += 1
            flag = 0
        if search_string in line:
            flag = 1
            insert_position = index + 1
        index += 1
    with open(filename, "w") as file:
        file.writelines(lines)
