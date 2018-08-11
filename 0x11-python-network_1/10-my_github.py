#!/usr/bin/python3
# takes your Github credentials (username and password)
# and uses the Github API to display your id
import requests
import sys


if __name__ == "__main__":

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(url, auth=(username, password))
    result = r.json().get('id')
    print(result)
