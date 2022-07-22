#!/usr/bin/python3
'''
This script contains a function that prints out a name

functions:
    say_my_name
'''

def say_my_name(first_name, last_name=""):
    '''
    Prints out a sentence

    params:
        first_name = person's first name / must be string
        last_name = person's last name (OPTIONAL) / must be string

    prints : My name is <first name> <last name>
    returns: Nothing
    '''
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print(f'My name is {first_name} {last_name}')

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
