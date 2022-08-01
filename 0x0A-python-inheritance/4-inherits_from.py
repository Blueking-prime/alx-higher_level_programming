#!/usr/bin/python3
'''
a function that checks the class of an object
'''


def inherits_from(obj, a_class):
    '''Checks if an object is an instance of a subclass of a class'''
    if obj.__class__ is not a_class:
        return isinstance(obj, a_class)
