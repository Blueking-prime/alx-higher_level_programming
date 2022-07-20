#!/usr/bin/python3
'''
Working With Classes
'''


class Square:
    '''This is a square
    it has a size and a position'''
    def __init__(self, size=0, position=(0, 0)):
        '''The __init__ function
        inittalizes attributes'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Creates a property of square called Size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Checks to see if size is an integer or not
        and also if it's less than 0'''
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def position(self):
        '''Creates a property of square called Position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Checks to see if Position is a tuple
        containing two positive integers'''
        self.__position = value
        try:
            if self.__position[0] < 0 or self.__position[1] < 0:
                raise TypeError
        except:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        '''Calculates and returns the Area of the square'''
        return self.__size * self.__size

    def my_print(self):
        '''Prints out a square to stdout
        also shifts it according to the position value'''
        if self.__size == 0:
            print('')
        else:
            if self.__position[1] > 0:
                print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
