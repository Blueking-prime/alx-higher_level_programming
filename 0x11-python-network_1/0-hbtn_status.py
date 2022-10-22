#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        cont_typ = type(body)
        decoded_str = body.decode('utf-8')
    print(f'Body response:\n\
    - type: {cont_typ}\n\
    - content: {body}\n\
    - utf8 content: {decoded_str}')
