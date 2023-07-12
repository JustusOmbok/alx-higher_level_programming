#!/usr/bin/python3
"""a class representing a student
"""
class Student:
    """
    defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary description"""
        if attrs is None:
            return self.__dict__
        else:
            filtered_attrs = {}
            for attr in attrs:
                if attr in self.__dict__:
                    filtered_attrs[attr] = self.__dict__[attr]
            return filtered_attrs
