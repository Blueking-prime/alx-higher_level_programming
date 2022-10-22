#!/usr/bin/python3
'''fetches a site'''


if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code:', r.status_code)
