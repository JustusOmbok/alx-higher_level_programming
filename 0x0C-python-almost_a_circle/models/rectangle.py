#!/usr/bin/python3
"""
Rectangle module - class rectangle defined
"""

from models.base import Base


class Rectangle(Base):
    """
    this class inherits from base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        A rectangle instance is initialized
        Args:
            width : the rectangle width
            height : the rectangle height
            x : the rectangle's x-coordinate
            y : the rectangles's y-coordinate
            id : the rectangle's id
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width attribute setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height attribute setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """x attribute setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """y attribute getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y attribute setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """displays triangle using '#'"""
        for _ in range(self.height):
            print('#' * self.width)
