#!/usr/bin/python3

"""Defines an integer definition function"""

def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int): First integer
        b (int): Second integer (default is 98)

    Returns:
        int:    The addition of a nd b

    Raises:
        TypeError: If b or a is not ant integer or float
        
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
