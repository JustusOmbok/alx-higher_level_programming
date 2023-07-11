#!/usr/bin/python3
"""
function that writes txt to file
"""

def append_write(filename="", text=""):
    """appends to a file and return num of characters"""
    if filename == "":
        return

    with open(filename, "a", encoding="utf8") as f:
        f.write(text)
    return len(text)
