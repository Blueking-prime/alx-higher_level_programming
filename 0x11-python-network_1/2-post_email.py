#!/usr/bin/python3
'''sends a post request to a url'''


if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')

    with urllib.request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
