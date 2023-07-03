#!/usr/bin/python3

def text_indentation(text):
    """
    prints a text with 2 lines

    Args:
        text (str): the text to be indented

    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    for char in characters:
        text = text.replace(char, f"{char}\n\n")

    print(text.strip())
