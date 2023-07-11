#!/usr/bin/python3

def read_file(filename=""):
    """Reads txt file prints the content

    Args:
        filename (str): name of file to be opened

    Returns:
        nothing
    """
    with open(filename, encoding='utf-8') as file:
        content = file.read()
        print(content, end='')

read_file()
