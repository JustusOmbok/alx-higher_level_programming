#!/usr/bin/python3

"""a class Square that defines a square"""

class Square:
    """class defines a square"""

    def __init__(self, size=0):
        """initilize square instance"""
        self.size = size

    @property
    def size(self):
        """getter method to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method to set size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


    def area(self):
        """returns current square area"""
        return self.__size ** 2
