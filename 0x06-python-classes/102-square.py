#!/usr/bin/python3

class Square(float):
    '''This is a square
    it has a size'''
    def __init__(self, size=0):
        '''The __init__ function'''
        self.size = size

    @property
    def size(self):
        '''Creates a property of square called Size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Checks to see if size is an integer or not
        and also if it's less than 0'''
        self.__size = value
        if type(self.__size) is not float and type(self.__size) is not int:
            raise TypeError('size must be a number')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''Calculates and returns the Area of the square'''
        return self.__size * self.__size
