#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i != x:
        try:
            print(f"{my_list[i]}", end="")
            i = i + 1
        except (ValueError, TypeError):
            continue
    finally:
        print("")
        return i
