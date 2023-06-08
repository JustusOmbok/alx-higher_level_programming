#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1

    if num_args == 0:
        print("0")
    else:
        result = sum(int(arg) for arg in argv[1:])
        print(result)
