#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    if len(argv) >= 2:
        for i in range(len(argv) - 1):
            value = int(argv[i + 1])
            sum += value
        print("{:d}".format(sum))
    else:
        print("{:d}".format(sum))
