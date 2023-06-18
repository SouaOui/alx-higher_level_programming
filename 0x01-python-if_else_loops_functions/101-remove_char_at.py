#!/usr/bin/python3
def remove_char_at(str, n):
    if str == "" or n > len(str) - 1:
        return str
    str_cpy = ""
    for i in range(len(str)):
        if i != n:
            str_cpy += str[i]
    return str_cpy
