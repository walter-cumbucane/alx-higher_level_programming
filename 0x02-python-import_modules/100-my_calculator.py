#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != "+" and argv[2] != "-" and argv[2] != "*" and argv[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        print(f"{a:d} + {b:d} = {add(a, b)}")
    elif argv[2] == "-":
        print(f"{a:d} - {b:d} = {sub(a, b)}")
    elif argv[2] == "*":
        print(f"{a:d} * {b:d} = {mul(a, b)}")
    else:
        print(f"{a:d} / {b:d} = {div(a, b)}")
