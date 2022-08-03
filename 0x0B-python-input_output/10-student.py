#!/usr/bin/python3
'''A class:
    Student'''


class Student():
    '''A class: students

    Instance Attributes:
        first_name
        last_name
        age

    methods:
        to_json(attrs[optional])'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a filtered dictionary representation
        of a Student instance'''
        new_dict = {}
        trigger = 0
        if type(attrs) is list:
            for i in attrs:
                if i not in self.__dict__:
                    continue
                new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__
