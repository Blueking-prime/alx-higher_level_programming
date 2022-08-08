#!/usr/bin/python3
'''Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    A square; subclass of Rectangle

    Instance attributes:
        size

    Methods:
        area
        display
        update

    __str__ returns a description of the object in th format:
        [class] (<id>) <x>/<y> - <width>/<height>
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        return f'[{self.__class__.__name__}] \
({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        '''Size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''Size setter'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Updtates an instance of Rectangle'''
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''Returns a dictionary descrription of a class'''
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }
