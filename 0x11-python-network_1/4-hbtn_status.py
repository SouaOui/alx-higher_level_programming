#!/usr/bin/python3
"""
    Write a Python script that fetches https://alx-intranet.hbtn.io/status
    - You must use the package requests
    - You are not allow to import packages other than requests
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    data = requests.get(url).text
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
