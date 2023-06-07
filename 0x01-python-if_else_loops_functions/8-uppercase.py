#!/usr/bin/python3
def uppercase(str):
    ret_str = ""
    for s in str:
        if (ord(s) >= 90 and ord(s) <= 122):
            ret_str += chr(ord(s) - 32)
        else:
            ret_str += s
    return ret_str
