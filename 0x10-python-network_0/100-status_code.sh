#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sI $1 | grep "HTTP/1.0" | cut -d " " -f2
