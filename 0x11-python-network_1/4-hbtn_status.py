#!/usr/bin/python3
'''fetches a site'''


if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')

    print(f'Body response:\n\
    - type: {type(r.text)}\n\
    - content: {r.text}')
