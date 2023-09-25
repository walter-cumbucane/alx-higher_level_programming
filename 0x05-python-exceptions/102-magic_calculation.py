#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 2):
        if i > a:
            raise Exception("Too far")
        else:
            intermedium = a ** b
        result += intermedium / i
    finally:
        result = a + b
        return result
