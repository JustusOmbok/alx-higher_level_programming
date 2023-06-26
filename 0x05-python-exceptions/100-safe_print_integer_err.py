#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        print("Exception: Unknown format code 'd' for object of type '{}'".format(value.__class__.__name__), file=sys.stderr)
        return False
