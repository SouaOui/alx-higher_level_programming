#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            result_str += chr(ord(c) - 32)
        else:
            result_str += chr(ord(c))
    return result_str


for index in range(ord('z'), ord('a') - 1, -1):
    if index % 2 != 0:
        index = ord(uppercase(chr(index)))
    print("{}".format(chr(index)), end="")
