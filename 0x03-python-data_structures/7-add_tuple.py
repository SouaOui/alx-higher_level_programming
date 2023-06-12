#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in range(2):
        tuple_a += (0, 0)
        tuple_b += (0, 0)
        new_tuple += (tuple_a[i] + tuple_b[i],)
    return new_tuple
