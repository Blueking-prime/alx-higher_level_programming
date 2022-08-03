#!/usr/bin/python3
'''
Returns a list of lists of integers representing pascal's triangle
'''


def f(n):
    '''Calculates factorial'''
    if n <= 1:
        return 1
    return n * f(n - 1)


def pascal_triangle(n):
    '''Creates Pascal's triangle'''
    if n <= 0:
        return []

    triangle = []

    for i in range(0, n):
        row = []
        k = -1
        while i != k:
            k += 1
            x = f(i) / (f(k) * f(i - k))
            row.append(int(x))
        triangle.append(row)

    return triangle
