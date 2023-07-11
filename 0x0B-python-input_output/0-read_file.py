#!/usr/bin/python3
"""defines a txt file-reading function"""

def read_file(filename=""):
    """Reads txt file prints the content

    Args:
        filename (str): name of file to be opened

    Returns:
        nothing
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
