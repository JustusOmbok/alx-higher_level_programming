#!/usr/bin/python3
"""a class Square that defines a square"""
class Square:
    """class defines square"""

    def __init__(self, size=0):
        """square instance is initialized"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns current square area"""
        return self.__size ** 2
