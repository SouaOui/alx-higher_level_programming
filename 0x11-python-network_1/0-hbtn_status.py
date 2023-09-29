#!/usr/bin/python3
"""
Write a Python script that fetches
https://alx-intranet.hbtn.io/status
"""


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as f:
    data = f.read().decode('utf-8')
    index = data.find('utf8 content:')
    print("Body response:")
    print("    - type: {}".format(type(data)))
    print("    - content: b'{}'".format(data))
    print("    - utf8 content: {}".format(data))

# index = data.find('utf8 content:')
# print(index)
# print(data)
# print(type(data))
# print(data)
