#!/usr/bin/python3
'''
A module containing a Rectangle Class

Methods:
    Area
    Perimeter
    __str__
    __repr__
'''


class Rectangle:
    '''
    This is a rectangle

    it has a:
        width
        height

    Instance methods:
        Area
        Perimeter

    Class attributes:
        number_of_instances

    __str__ returns a string that arranges into a rectangle
    made of print_symbol characters
    __repr__ returns a string that contains
    all the useful information about the object
    __del__ prints out 'Bye rectangle...' to stdout
    and decrements the number_of_instances
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        text = ''
        if self.width == 0 or self.height == 0:
            text = ''
        else:
            for i in range(self.height):
                text += str(self.print_symbol) * self.width
                if i < self.height - 1:
                    text += '\n'
        return text

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Calulates the area of the Rectangle'''
        return self.height * self.width

    def perimeter(self):
        '''Calulates the perimeter of the Rectangle'''
        per = 2 * (self.height + self.width)
        if self.height == 0 or self.width == 0:
            per = 0
        return per
