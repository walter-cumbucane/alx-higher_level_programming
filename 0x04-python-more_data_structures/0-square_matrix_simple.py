#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_matrix = list()
    for row in matrix:
        roww = []
        for number in row:
            squared = number ** 2
            roww.append(squared)
        new_matrix.append(roww)
    return new_matrix
