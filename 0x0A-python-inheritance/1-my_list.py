#!/usr/bin/python3
'''
Contains a subclass of list
'''


class MyList(list):
    '''A subclass of list'''
    def print_sorted(self):
        '''Prints the list in ascending order'''
        l = list(self[:])
        l.sort()
        print(l)


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/1-my_list.txt')
