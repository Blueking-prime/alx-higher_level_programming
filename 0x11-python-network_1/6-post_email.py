#!/usr/bin/python3
'''posts data to a site'''


if __name__ == '__main__':
    import requests
    import sys

    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
