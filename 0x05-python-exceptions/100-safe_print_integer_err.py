#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError as ve:
        if "format code 'd'" in str(ve):
            print("Exception: Unknown format code 'd' for object of type 'str'", file=sys.stderr)
        else:
            print("Exception: ValueError", file=sys.stderr)
        return False
    except TypeError:
        print("Exception: TypeError", file=sys.stderr)
        return False
