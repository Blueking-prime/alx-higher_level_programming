#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit

    j = len(argv)
    
    if j == 1:
        print("0 arguments.")
        exit()

    print(f"{j- 1} argument", end=':\n' if j == 2 else 's:\n')
    for i in range(j):
        if i == 0:
            continue
        print(f"{i}: {argv[i]}")
