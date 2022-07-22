#!/usr/bin/python3
'''
This script contains a function that prints out a square

functions:
    print_square
'''

def print_square(size):
    '''
    Prints out a square

    params:
        size =  length of the square

    prints : square comprised of # charcters
    returns: Nothing
    '''
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
