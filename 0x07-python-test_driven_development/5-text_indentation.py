#!/usr/bin/python3
'''
This script contains a function that prints out formatted text

functions:
    text_indentation
'''

def text_indentation(text):
    '''
    Prints out the text but
    with 2 new lines after each of these characters:
         ., ? and :

    params:
        text =  text to be formatted

    prints : formatted text
    returns: Nothing
    '''
    if type(text) is not str:
        raise TypeError('text must be a string')

    t_l = list(text)
    for i in range(len(t_l)):
        if t_l[i] == '.' or t_l[i] == '?' or t_l[i] == ':':
            try:
                if t_l[i + 1] == ' ':
                    t_l[i] += '\n'
                    t_l[i + 1] = '\n'
                else:
                    t_l[i] += '\n\n'
            except IndexError:
                t_l[i] += '\n'

    print(''.join(t_l))

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
