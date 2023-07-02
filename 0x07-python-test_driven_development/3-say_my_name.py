#!/usr/bin/python3
"""Defines function to print first and last name"""

def say_my_name(first_name, last_name=""):
    """
    prints "My name is <first name> <last name>"

    Args:
        first_name (str): the first name
        last_name (str, optional): the last name

    Raises:
        TypeError: If either first_name or last_name is not a string
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name).strip())
