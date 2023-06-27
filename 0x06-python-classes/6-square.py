#!/usr/bin/python3

"""a class Square that defines a square"""
class Square:
    """class defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize square instance"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter method to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method to set position"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of two positive integers")
        else:
            self.__position = value

    def area(self):
        """prints the square with char #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
