#!/usr/bin/python3
'''
Working With Classes
'''


class Node:
    '''This is a Node in a linked list'''
    def __init__(self, data, next_node=None):
        '''The __init__ function
        inittalizes attributes'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''Creates a property of Node called Data'''
        return self.__data

    @data.setter
    def data(self, value):
        '''Checks to see if size is an integer or not
        and also if it's less than 0'''
        self.__data = value
        if type(self.__data) is not int:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        '''Creates a property of Node called next_node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Checks to see if next_node is a Node'''
        self.__next_node = value
        if type(self.__next_node) is not Node and self.__next_node is not None:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    '''This Creates a linked list'''
    def __init__(self):
        '''The __init__ function
        inittalizes attributes'''
        self.__head = None

    def __str__(self):
        '''Prints out the list'''
        text = ''
        current = self.__head
        while current.next_node:
            text += str(current.data)
            text += '\n'
            current = current.next_node

        text += str(current.data)
        return text

    def sorted_insert(self, value):
        '''Adds sorted nodes to a list'''
        if self.__head is None:
            self.__head = Node(value)
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                previous = current
                current = current.next_node
            if current.next_node is None:
                current.next_node = Node(value)
            elif current is self.__head:
                self.__head = Node(value, current)
            else:
                new = Node(value, current.next_node)
                current.next_node = new
    '''
def sorted_insert(self, value):
    if self.__head is None:
        self.__head = Node(value)
    else:
        current = self.__head
        previous = None
        while current and value > current.data:
            previous = current
            current = current.next_node
        if current is None:
            previous.next_node = Node(value)
        elif current is self.__head and previous is None:
            self.__head = Node(value, current)
        else:
            newNode = Node(value, current)
            previous.next_node = newNode'''
