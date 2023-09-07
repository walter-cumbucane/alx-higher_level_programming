#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    number_arguments = len(argv) - 1
    if number_arguments == 0:
        print(f"{number_arguments:d} arguments.")
    else:
        print(f"{number_arguments:d} arguments:")
        i = 1
        while i <= number_arguments:
            print(f"{i:d}: {argv[i]}")
            i = i + 1
