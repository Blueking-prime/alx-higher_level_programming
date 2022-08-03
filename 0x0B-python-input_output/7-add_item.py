#!/usr/bin/python3
'''Load object from JSON file'''
import json
import sys


def save_to_json_file(my_obj, filename):
    '''Saves an Object to a JSON file'''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    '''Loads an Object from a JSON file'''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


filename = 'add_item.json'
try:
    arg_list = load_from_json_file(filename)
except FileNotFoundError:
    arg_list = []
finally:
    i = 1
    try:
        while True:
            arg_list.append(sys.argv[i])
            i += 1
    except IndexError:
        pass
    finally:
        save_to_json_file(arg_list, filename)
