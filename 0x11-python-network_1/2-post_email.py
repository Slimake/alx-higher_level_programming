#!/usr/bin/python3
"""
2-post_email

Contains a Python script that takes in a URL and an email, sends a POST \
request to the passed URL with the email as a parameter, and displays the \
body of the response (decoded in utf-8)
"""

import urllib.request
from sys import argv

# Only run when the script is not imported
if __name__ == '__main__':
    url = argv[1]
    values = {}
    values['email'] = argv[2]

    # encoding data
    data = urllib.parse.urlencode(values)
    # data should be in btye
    data = data.encode('ascii')
    # Fetch data from URL
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
