#!/usr/bin/python3
"""
1-hbtn_header

Contains a Python script that takes in a URL, sends a request to \
the URL and displays the value of X-Request-Id variable found in \
the header of the response.
"""

import urllib.request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    # Fetch data from URL
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
