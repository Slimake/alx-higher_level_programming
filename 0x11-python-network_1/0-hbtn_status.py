#!/usr/bin/python3
"""
0-hbtn_status module

Contains a Python script that fetches a URL
"""

import urllib.request

if __name__ == '__main__':
    # Fetch data from URL
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('utf-8')))
