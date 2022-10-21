#!/usr/bin/python3
'''Finds the peak of an array'''


def find_peak(list_of_integers):
    '''Goes through list to find the peak'''
    if type(list_of_integers) is not list:
        return None
    if len(list_of_integers) == 0:
        return None
    a = list_of_integers[0]
    for i in list_of_integers:
        if i > a:
            a = i
    return a
