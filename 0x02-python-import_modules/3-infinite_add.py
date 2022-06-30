#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    j = len(argv)
    k = 0

    if j == 1:
        print(0)
        exit()

    for i in range(j):
        if i == 0:
            continue
        k += int(argv[i])

    print(k)
