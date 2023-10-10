#!/usr/bin/python3
"""This module contains a function that writes to a file"""


def write_file(filename="", text=""):
    """This functions writes and returns the num of chars written to a file"""
    with open(filename, "w", encoding="utf-8") as file:
        written_characters = filename.write(text)
    return written_characters
