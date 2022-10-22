#!/usr/bin/python3
'''sends a post request to a JSON site'''


if __name__ == '__main__':
    import requests
    import sys

    if sys.argv[1]:
        value = {'q': sys.argv[1]}
    else:
        value = {'q': ''}
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=value)
        if r.json() == {}:
            print('No result')
        key = r.json().keys()[0]
        key_val = r.json().get(key)
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
    else:
        display_str = f'[{key}] {key_val}'
        print(display_str)
