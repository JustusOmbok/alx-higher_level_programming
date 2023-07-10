#!/usr/bin/python3
"""
class with a area method that raises an exception
"""
class BaseGeometry:
    """ class that raises an exception"""
    def area(self):
        """
        area method that raises an exception
        """
        raise Exception("area() is not implemented")
