#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise ValueError
    except ValueError:
        print("Exception: Unknown format code 'd' for object of type '{}'".format(value.__class__.__name__), file=sys.stderr)
        return False
