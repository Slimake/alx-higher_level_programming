#!/usr/bin/python3
"""
6-post_email

Contains a Python script that takes in a URL and an email, sends a POST \
request to the passed URL with the email as a parameter, and displays the \
body of the response
"""

import requests
from sys import argv

# Only run when the script is not imported
if __name__ == '__main__':
    url = argv[1]
    values = {}
    values['email'] = argv[2]

    # Fetch data from URL
    r = requests.post(url, data=values)
    print(r.text)
