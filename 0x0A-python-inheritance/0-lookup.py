#!/usr/bin/python3
'''Contains a function that looks-up the attributes of an object'''


def lookup(obj):
    '''Returns a list of all the attributes
    of an object'''
    return list(dir(obj))
