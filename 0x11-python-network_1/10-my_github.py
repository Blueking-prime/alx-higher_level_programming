#!/usr/bin/python3
'''sends a post request to a JSON site'''


if __name__ == '__main__':
    import requests
    import sys

    url = 'https://api.github.com/user'
    cred = (sys.argv[1], sys.argv[2])

    r = requests.get(url, auth=cred)

    print(r.json().get('id'))
