#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    logic_value = list()
    for num in my_list:
        if num % 2 == 0:
            logic_value.append(True)
        else:
            logic_value.append(False)
    return logic_value
