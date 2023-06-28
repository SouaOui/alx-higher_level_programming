#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as say:
        sys.stderr.write("Exception: {}\n".format(say))
        return False
