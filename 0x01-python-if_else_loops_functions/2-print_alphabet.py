#!/usr/bin/python3

for char in range(97, 123):
    print("{}".format(chr(char)), end="")
    if (char == 122):
        print("\n", end="")
