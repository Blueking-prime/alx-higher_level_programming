#!/usr/bin/python3
'''Reads a file'''


def read_file(filename=""):
    '''Reads from a file'''
    with open(filename, encoding='utf-8') as f:
        print(f.read())
