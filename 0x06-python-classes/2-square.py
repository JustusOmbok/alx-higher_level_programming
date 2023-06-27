#!/usr/bin/python3

"""a class Square that defines a square by: (based on 1-square.py)"""

class Square:
    """Class defines a square"""

    def __init__(self, size=0):

        """Square instance is initialized"""
        if not isinstance(size, int):
            raise TypeErrorr("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
