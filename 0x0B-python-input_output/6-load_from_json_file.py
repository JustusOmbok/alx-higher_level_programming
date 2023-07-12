#!/usr/bin/python3
"""
program create an object from json file
"""
import json
def load_from_json_file(filename):
    """
    a function creates an object from json file
    """
    with open(filename, 'r', encoding="utf8")as file:
        return json.load(file)
