#!/usr/bin/python3
"""
10-my_github

A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv


if __name__ == '__main__':
    username = argv[1]
    token = argv[2]

    url = "https://api.github.com/users/{}".format(username)
    headers = {'Authorization': token}
    try:
        r = requests.get(url, headers=headers)
        print(r.json()['id'])
    except KeyError:
        print(None)
