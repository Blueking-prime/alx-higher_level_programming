#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a = [0, 0]
    l_b = [0, 0]

    j = 0
    for i in tuple_a:
        l_a[j] = i
        j += 1

    j = 0
    for i in tuple_b:
        l_b[j] = i
        j += 1

    res = (l_a[0] + l_b[0], l_a[1] + l_b[1])

    return res
