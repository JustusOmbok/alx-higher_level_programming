#!/usr/bin/python3
def lookup(obj):
    """
    Returns list of attributes available and methods of an object
    Args:
        obj: the object to be looked up
    Returns:
        A list of attribute and method names

    """
    return dir(obj)
