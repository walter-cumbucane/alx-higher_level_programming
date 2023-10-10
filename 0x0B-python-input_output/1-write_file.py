#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            characters_written = file.write(text)
        return characters_written
    else:
        return 0
