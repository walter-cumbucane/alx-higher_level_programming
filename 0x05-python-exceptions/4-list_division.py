#!/usr/bin/python3

def list_division(my_list1, my_list2, list_length):
    i = 0
    result = list()
    while i != list_length:
        try:
            element = my_list1[i] / my_list2[i]
            result.append(element)
            i += 1
            continue
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
            i += 1
            continue
        except TypeError:
            print("wrong type")
            result.append(0)
            i += 1
            continue
        except (ValueError, IndexError):
            print("out of range")
            result.append(0)
            i += 1
            continue
        finally:
            if i == list_length:
                return result
