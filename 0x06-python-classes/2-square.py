#!/usr/bin/python3

class Square:
    '''This is a square
    it has a size'''
    def __init__(self, size=0):
        '''The __init__ function

        Checks to see if size is an integer or not
        and also if it's less than 0'''
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
