#!/usr/bin/python3
"""
the BaseGeometry class is defined with the area and integer_validator methods
"""
class BaseGeometry:
    """
    class is defined with the area and integer_validator
    """
    def area(self):
        """
        area method raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        checks if value is an integer
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
