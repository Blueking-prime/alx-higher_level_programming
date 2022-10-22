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
        id = r.json().get('id')
        name = r.json().get('name')
    except ValueError:
        print('Not a valid JSON')
    else:
        display_str = f'[{id}] {name}'
        print(display_str)
