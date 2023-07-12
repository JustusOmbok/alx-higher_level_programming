#!/usr/bin/python3
"""
a class Student that defines a student
"""
class Student:
    """a class that represents a student"""
    def __init__(self, first_name, last_name, age):
        """a new instance is initialised"""
        self.first_name = first_name
        self.lastname = last_name
        self.age = age

    def to_json(self):
        """
        a dict representation is retrieved
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
