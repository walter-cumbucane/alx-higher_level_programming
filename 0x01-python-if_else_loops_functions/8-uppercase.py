#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

def uppercase(str):
    for char in str:
        character = ord(char)
        if islower(char):
            character = character - 32
            print("{}".format(chr(character)), end="")
            continue
        print("{}".format(char), end="")
    print("", end="\n")
