#!/usr/bin/python3
"""
Write a Python script that fetches
https://alx-intranet.hbtn.io/status
"""


import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as f:
    data = f.read()
    result_decode = data.decode('UTF-8')
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(result_decode))

# index = data.find('utf8 content:')
# print(index)
# print(data)
# print(type(data))
# print(data)
