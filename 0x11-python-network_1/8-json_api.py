#!/usr/bin/python3
#  that takes in a letter and sends a POST request to
# http://0.0.0.0:5000/search_user with the letter as a parameter.
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 2:
        r = requests.post('http://0.0.0.0:5000/search_user',
                          data={'q': sys.argv[1]})
    else:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ""})
    try:
        if r.json() == {}:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    except:
        print("Not a valid JSON")
