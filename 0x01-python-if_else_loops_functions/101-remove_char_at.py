#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    word = ""
    for char in str:
        if i == n:
            i = i + 1
            continue
        word += char
        i = i + 1
    return word
