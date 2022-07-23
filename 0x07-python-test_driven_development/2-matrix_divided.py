#!/usr/bin/python3
'''
This script contains a function that divides a matrix by a scalar number

functions:
    matrix_divided
'''

def matrix_divided(matrix, div):
    '''
    Divides a matrix by a number (div)

    params:
        matrix = a list of lists of integers/floats
        div = an integer/float that divides the matrix

    prints : nothing
    returns: A new matrix with the results
    '''
    err1 = 'Each row of the matrix must have the same size'
    err2 = 'matrix must be a matrix (list of lists) of integers/floats'

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    try:
        len(matrix[0]);
    except TypeError:
        raise TypeError(err2)

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError(err1)
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(err2)

    new_matrix = [x[:] for x in matrix]
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)

    return new_matrix

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
