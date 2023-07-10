#!/usr/bin/python3
"""
A class inheriting from basegeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """class that inherrits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """returns rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height
