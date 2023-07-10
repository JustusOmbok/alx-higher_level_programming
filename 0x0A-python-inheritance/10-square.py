#!/usr/bin/python3
"""
class Square that inherits from Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Square class is defined as a subclass of Rectangle
    """
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        provides a custom string representation of the Square object
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
