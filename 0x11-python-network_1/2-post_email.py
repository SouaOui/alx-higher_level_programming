#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


import sys
import urllib.request
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data_encoded = urllib.parse.urlencode(email).encode('utf-8')
    try:
        response = urllib.request.Request(url, data_encoded, method='POST')
        with urllib.request.urlopen(response) as f:
            response = f.read().decode('utf-8')
            print(response)
    except Exception as f:
        print('An Error Occured :{}'.format(f))
