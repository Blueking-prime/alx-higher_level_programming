#!/usr/bin/python3
'''
This contains a function that adds 2 numbers and returns an integer

functions:
    add_integer
'''

def add_integer(a, b=98):
    '''
    Adds 2 numbers and returns an integer

    if only one number is given, 98 is added by default
    '''
    if type(a) is not float and type(a) is not int:
        raise TypeError('a must be an integer')
    if type(b) is not float and type(b) is not int:
        raise TypeError('b must be an integer')

    return int(a) + int(b)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
