#!/usr/bin/python3
'''
Contains a class:
    BaseGeometry
'''


class BaseGeometry():
    '''A class: BaseGeometry

    Attributes:
        none
    Methods:
        area
        integer_validator
    '''

    def area(self):
        '''Calculates area of the shape'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates whether value is an integer'''
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/7-base_geometry.txt')
