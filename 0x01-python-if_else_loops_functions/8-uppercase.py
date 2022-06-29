#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) <= 122 and ord(str[i]) >= 97:
            j = chr(ord(str[i]) - 32)
        else:
            j = chr(ord(str[i]) - 32)
        print("{}".format(j), end='')
    print('')
