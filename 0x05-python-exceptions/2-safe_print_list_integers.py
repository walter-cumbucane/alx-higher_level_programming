#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        while i != x:
            print(f"{my_list[i]}", end="")
            i = i + 1
    except (ValueError, TypeError):
        pass
    finally:
        print("")
        return i
