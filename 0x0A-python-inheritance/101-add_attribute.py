#!/usr/bin/python3
'''
A function that adds an attribute
'''


def add_attribute(obj, name, value):
    '''Adds an attribute to a function'''
    if isinstance(obj, (int, str, float, dict, list, BaseException, tuple)):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
