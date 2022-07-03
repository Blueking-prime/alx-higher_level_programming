#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a = [0, 0]
    l_b = [0, 0]

    j = 0
    for i in tuple_a:
        if i is None:
            l_a[j] = 0
        else:
            l_a[j] = i
        j += 1

    j = 0
    for i in tuple_b:
        if i is None:
            l_b[j] = 0
        else:
            l_b[j] = i
        j += 1

    return (l_a[0] + l_b[0], l_a[1] + l_b[1])
