#!/usr/bin/python3
def new_in_list(my_list, idx, element):
     cpy = my_list[:]

    length = len(my_list)

    if 0 < idx > length - 1:
        return cpy[idx] = element
    return cpy
