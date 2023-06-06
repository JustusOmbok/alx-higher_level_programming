#!/usr/bin/python3
def uppercase(string):
    for c in string:
        uppercase_char = chr(ord(c) -32) if ord(c) >= 97 and ord(c) <= 122 else c
        print(uppercase_char, end='')
    print()
