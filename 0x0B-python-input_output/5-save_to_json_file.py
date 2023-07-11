#!/usr/bin/python3
"""
program saves json file to a text file
"""
import json
def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    """
    if filename == "":
        return
    with open(filename, "w") as f:
        json.dump(my_obj, f)
