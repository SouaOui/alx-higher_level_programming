#!/usr/bin/python3
def uppercase(str):
    ret_str = ""
    for c in str:
        if (ord(c) >= 90 and ord(c) <= 122):
            ret_str += chr(ord(c) - 32)
        else:
            ret_str += c
    print("{}".format(ret_str))
