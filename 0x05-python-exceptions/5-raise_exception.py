#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Raise this exception")
    except Exception:
        print("exception Raised")
