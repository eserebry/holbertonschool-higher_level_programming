#!/usr/bin/python3
# takes in a URL, sends a request to the URL
# and displays the body of the response (decoded in utf-8).
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except Response.raise_for_status as e:
        print("Error code: {}".format(e.status_code))
