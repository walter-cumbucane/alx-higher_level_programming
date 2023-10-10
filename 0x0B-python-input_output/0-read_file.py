#!/usr/bin/python3
"""This module contains a function that reads a file"""


def read_file(filename=""):
    """THis function reads a file and prints it to the stdout"""
    if filename:
        file = open(filename, "r", encoding="utf-8")
        print(file.read().rstrip())
