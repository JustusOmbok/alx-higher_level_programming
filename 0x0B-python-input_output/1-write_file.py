#!/usr/bin/python3
"""writes a string to a txt file"""

def write_file(filename="", text=""):
    """
    returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        characters_written = file.write(text)

    return characters_written
