#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        tuple_result = (0, 0)
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        tuple_result = (tuple_a[0] + tuple_b[0], 0)
    elif len(tuple_a) == 0 and len(tuple_b) == 1:
        tuple_result = (tuple_b[0], 0)
    elif len(tuple_a) == 1 and len(tuple_b) == 0:
        tuple_result = (tuple_a[0], 0)
    elif len(tuple_a) == 2 and len(tuple_b) == 0:
        tuple_result = tuple_a
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        tuple_result = (tuple_a[0] + tuple_b[0], tuple_a[1])
    elif len(tuple_a) == 0 and len(tuple_b) == 2:
        tuple_result = tuple_b
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        tuple_result = (tuple_a[0] + tuple_b[0], tuple_b[1])
    else:
        tuple_result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_result
