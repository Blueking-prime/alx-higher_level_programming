#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_list = [x for x in a_dictionary]
    new_list.sort()

    for i in new_list:
        print(f"{i}: {a_dictionary.get(i)}")
