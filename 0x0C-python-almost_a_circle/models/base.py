#!/usr/bin/python3
"""
Base module - base class is defined
"""
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json string of a dictionary
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        json string representation of list_objs is written to file
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        list represented by json string is returned
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """
        an instance with all attibutes is returned
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy
