#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    if idx > len(my_list) - 1:
        return my_list

    list_2 = my_list[:]
    list_2[idx] = element
    return list_2
