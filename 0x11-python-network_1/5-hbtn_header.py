#!/usr/bin/python3
"""  document goes here """
import requests
import sys

if __name__ == "__main__":
    Url = sys.argv[1]
    response = requests.get(Url)
    print(response.headers.get("X-Request-Id"))