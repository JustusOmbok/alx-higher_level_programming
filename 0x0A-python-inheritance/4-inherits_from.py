#!/usr/bin/python3
"""checks if the type of object is a subclass
"""
def inherits_from(obj, a_class):
    """
    second part ensures object an instance of the class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
