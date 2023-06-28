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

    @property
    def position(self):
        """getter method to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method to set the position"""
        if(
                not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(coord, int) for coord in value)
                or any(coord < 0 for coord in value)
            ):

                raise TypeError("position must be a tuple")
            self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints the square with character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """returns a string representation of the square"""
        square_str = ""
        if self.size == 0:
            return square_str
        else:
            for _ in range(self.position[1]):
                square_str += "\n"
            for _ in range(self.size):
                square_str += " " * self.position[0] + "#" * self.size + "\n"
            return square_str.rstrip()
