#!/usr/bin/python3
'''fetches a header from a site'''


if __name__ == '__main__':
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
