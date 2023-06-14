#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, y in list(a_dictionary.items()):
        if y == value:
            del a_dictionary[key]
    return a_dictionary

