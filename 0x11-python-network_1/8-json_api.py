#!/usr/bin/python3
"""
8-json_api

Script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

# Only run when the script is not imported
if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    # Fetch data from URL
    payload = {'q': q}
    r = requests.post(url, data=payload)
    try:
        obj = r.json()
        if obj:
            print("[{}] {}".format(obj['id'], obj['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
