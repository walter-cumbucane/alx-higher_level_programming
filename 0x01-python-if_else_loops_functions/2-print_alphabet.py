#!/usr/bin/python3

for char in range(97, 123):
    if char == 122:
        print(f"{char:c}")
        break
    print(f"{char:c}", end="")
