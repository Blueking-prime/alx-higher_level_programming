#!/usr/bin/python3
'''Load object from JSON file'''


def class_to_json(obj):
    '''returns the dictionary description of an object'''
    return obj.__dict__
