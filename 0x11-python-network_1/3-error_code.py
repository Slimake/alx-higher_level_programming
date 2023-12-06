#!/usr/bin/python3
"""
3-error_code

Contains a Python script that takes in a URL, sends a request to the \
URL and displays the body of the response (decoded in utf-8).
"""

import urllib.request
from sys import argv

# Only run when the script is not imported
if __name__ == '__main__':
    url = argv[1]
    # Fetch data from URL
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
