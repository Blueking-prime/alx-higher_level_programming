#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    new_dict = {a_dictionary[x] : x for x in a_dictionary}
    new_list = sorted([x for x in new_dict])

    return new_dict[new_list[-1]]
