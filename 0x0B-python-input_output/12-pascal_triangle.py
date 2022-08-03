#!/usr/bin/python3
'''
Returns a list of lists of integers representing pascal's triangle
'''


def factorial(n):
    '''Calculates factorial'''
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def pascal_triangle(n):
    '''Creates Pascal's triangle'''
    if n <= 0:
        return []

    triangle = []

    for i in range(1, n + 1):
        row = []
        k = 0
        while i != k:
            x = factorial(i) / (factorial(i) - factorial(k))
            row.append(int(x))
            k += 1
        triangle.append(row)

    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


print((factorial(5) - factorial(2))/factorial(5-2))