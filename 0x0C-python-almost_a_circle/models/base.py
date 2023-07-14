#!/usr/bin/python3
"""
Base module - base class is defined
"""

class Base:
    """
    class to manage id attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        base instance is initialized

        Args:
            id(int): instance id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
