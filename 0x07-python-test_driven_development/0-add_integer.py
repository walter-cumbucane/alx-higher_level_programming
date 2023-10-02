#!/usr/bin/python3
"""This module contains a function that adds two numbers"""


def add_integer(a, b=98):
    """adds two numbers
        Args:
            a(int/ float): number to sum up
            b(int/float): number to sum up
        Returns:
            the addition of the two numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
