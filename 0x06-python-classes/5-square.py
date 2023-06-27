#!/usr/bin/python3

"""a class Square that defines a square"""

class Square:
    """class defines a square"""

    def __init__(self, size=0):
        """initialize square instance"""
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

    def my_print(self):
        """prints the square with char #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
