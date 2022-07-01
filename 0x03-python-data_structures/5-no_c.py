#!/usr/bin/python3
def no_c(my_string):
    str_list = []

    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        str_list.append(i)

    new_string = ''.join(str_list)
    return new_string
