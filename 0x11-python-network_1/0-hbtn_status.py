#!/usr/bin/python3
'''fetches https://alx-intranet.hbtn.io/status'''


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        cont_typ = type(body)
        decoded_str = body.decode('utf-8')

    str1 = f'Body response:\n\t- type: {cont_typ}\n'
    str2 = f'\t- content: {body}\n\t- utf8 content: {decoded_str}'
    print(str1 + str2)
