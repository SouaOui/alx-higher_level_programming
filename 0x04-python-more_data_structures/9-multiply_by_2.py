#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return dict(list(map(lambda x, y: (x, y * 2),
                         a_dictionary.keys(), a_dictionary.values())))
