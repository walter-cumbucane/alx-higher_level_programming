#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) - 1 == 0:
        print("0")
    else:
        i = 1
        result = 0
        while i <= len(argv) - 1:
            result += int(argv[i])
            i = i + 1
        print("{:d}".format(result))
