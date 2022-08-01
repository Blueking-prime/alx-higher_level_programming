#!/usr/bin/python3
'''
Contains two classes:
    BaseGeometry
    Rectangle
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


class Rectangle(BaseGeometry):
    '''A class: Rectangle
    subclass of BaseGeometry

    Attributes:
        __width
        __height
    Methods:
        area
        integer_validator
    '''
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f'[{self.__class__.__name__}] {self.__width}/{self.__height}'

    def area(self):
        '''returns the area of the rectangle'''
        return self.__width * self.__height
