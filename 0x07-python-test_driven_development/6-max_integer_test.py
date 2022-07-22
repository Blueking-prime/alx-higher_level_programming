#!/usr/bin/python3
'''
This script contains a function that
finds the biggest integer in a list

functions:
    max_integer
'''

def max_integer(list=[]):
    '''
    Finds th biggest integer in a list

    params:
        list =  list to be searched

    prints : Nothing
    returns: The biggest number
    '''
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
