#!/usr/bin/python3
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    num = int(sys.argv[1])
except Exception as e:
    print("N must be a number")
    exit(1)
if num < 4:
    print("N must be at least 4")
    exit(1)
