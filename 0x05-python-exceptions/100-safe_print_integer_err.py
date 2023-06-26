#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        print("Exception: ValueError", file=sys.stderr)
        return False
    except TypeError:
        print("Exception: TypeError", file=sys.stderr)
        return False
