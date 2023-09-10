#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for lst in matrix:
            for num in lst:
                print("{:d}".format(num), end="\n" if num == lst[-1] else " ")
