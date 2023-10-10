#!/usr/bin/python3
"""This module contains a functions that appends text to a file"""


def append_write(filename="", text=""):
    """This function appends text and returns the num of chars written to a file"""
    with open(filename, "a", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written
