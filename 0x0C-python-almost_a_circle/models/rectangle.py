#!/usr/bin/python3
'''Rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''
    A rectangle; subclass of Base

    Instance attributes:
        __width
        __height
        __x
        __y

    Methods:
        area
        display
        update

    __str__ returns a description of the object in th format:
        [class] (<id>) <x>/<y> - <width>/<height>
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return f'[{self.__class__.__name__}] \
({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

    @property
    def width(self):
        '''Width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Width setter'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Height setter'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''X getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''X setter'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''Y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Y setter'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Returns the area of thr rectangle'''
        return self.width * self.height

    def display(self):
        '''prints out a representation of the rectangle'''
        print('\n' * self.y, end='')
        for i in range(self.height):
            print((' ' * self.x) + ('#' * self.width))

    def update(self, *args, **kwargs):
        '''Updtates an instance of Rectangle'''
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                return
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns a dictionary descrription of a class'''
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
