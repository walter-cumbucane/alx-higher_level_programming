#!/usr/bin/python3

i = 1
char = 90

while (char >= 65):
    if (i % 2 != 0):
        character = char + 32
    else:
        character = char
    print("{}".format(chr(character)), end="")
    char = char - 1
    i = i + 1
