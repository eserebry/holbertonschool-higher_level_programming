#!/usr/bin/python3
# takes in a string and sends a search request to the Star Wars API
import requests
import sys


if __name__ == "__main__":

    url = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    r = requests.get(url)
    result = r.json().get('results')
    count = r.json().get('count')
    print("Number of results: {}".format(count))
    for i in result:
        print("{}".format(i.get('name')))
