#!/usr/bin/python3
# takes in a URL, sends a request to the URL
# and displays the body of the response (decoded in utf-8).
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            utf_8 = the_page.decode('utf-8')
        print(utf_8)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
