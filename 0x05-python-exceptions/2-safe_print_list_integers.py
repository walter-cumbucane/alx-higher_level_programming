#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        printed_element = 0
        while i != x:
            if isinstance(my_list[i], int):
                print(f"{my_list[i]}", end="")
                printed_element = printed_element + 1
                i = i + 1
            else:
                i = i + 1
                continue
    except (ValueError):
        pass
    finally:
        print("")
        return printed_element
