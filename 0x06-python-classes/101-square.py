#!/usr/bin/python3
"""Write a class Square that defines a square"""
class Square:
    """class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a square instance"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method to set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
