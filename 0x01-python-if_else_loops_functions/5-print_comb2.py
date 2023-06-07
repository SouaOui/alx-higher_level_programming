#!/usr/bin/python3
for num in range(100):
    if num // 10 != 9 and num % 10 != 9:
        print("{:d}, ".format(num), end="")
    elif num == 99:
        print(num)
