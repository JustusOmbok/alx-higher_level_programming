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
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """returns current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with char #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
