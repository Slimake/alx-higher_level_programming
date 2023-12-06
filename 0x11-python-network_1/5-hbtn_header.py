#!/usr/bin/python3
"""
5-hbtn_header

Contains a Python script that takes in a URL, sends a request to \
the URL and displays the value of X-Request-Id variable found in \
the header of the response.
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    # Fetch data from URL
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
