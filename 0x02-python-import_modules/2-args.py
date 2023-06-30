#!/usr/bin/python3
from sys import argv

len = len(argv)-1
if len == 0:
    print("0: Arguments.")
elif len == 1:
    print("{} argument:\n{}: {}".format(len, len, argv[len]))
else:
    print("{} arguments:".format(len))
    for i in range(len):
        print("{}: {}".format(i+1, argv[i + 1]))
