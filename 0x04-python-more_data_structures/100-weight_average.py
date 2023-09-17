#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerador = 0
    denominador = 0
    average = 0
    for number, weight in my_list:
        numerador += number * weight
        denominador += weight
    average = numerador / denominador
    return average
