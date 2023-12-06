#!/usr/bin/python3
"""
7-error_code

Contains a Python script that takes in a URL, sends a request \
to the URL and displays the body of the response
"""

import requests
from sys import argv

# Only run when the script is not imported
if __name__ == '__main__':
    url = argv[1]
    # Fetch data from URL
    try:
        with requests.get(url) as r:
            print(r.text)
    except requests.raise_for_status() as e:
        print("Error code: {}".format(e.code))
