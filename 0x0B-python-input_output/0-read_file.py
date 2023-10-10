#!/usr/bin/python3
"""This module contains a function that reads a file"""


def read_file(filename=""):
    """THis function reads a file and prints it to the stdout"""
    if filename:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read().strip())
            file.close()
