#!/usr/bin/python3
'''Saves object to JSON file'''
import json


def save_to_json_file(my_obj, filename):
    '''Saves an Object to a JSON file'''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
