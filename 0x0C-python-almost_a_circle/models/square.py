#!/usr/bin/python3
"""
square module - the Square class is defined
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        A Square instance is initialized
        Args: size, x, y, id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size attribute getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size attribute setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        string representation of the Square instance is returned
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        attributes of the square base are updated
        """
        if len(args) > 0:
            attributes = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns square instance attributes as a dictionary
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
