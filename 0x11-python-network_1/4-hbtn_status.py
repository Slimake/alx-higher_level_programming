#!/usr/bin/python3
"""
4-hbtn_status module

Contains a Python script that fetches a URL
"""

import requests

if __name__ == '__main__':
    # Fetch data from URL
    r = requests.get('https://alx-intranet.hbtn.io/status')

    body = r.text
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
