#!/usr/bin/python3
"""
Base module - base class is defined
"""
import json

import csv

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


    @classmethod
    def load_from_file(cls):
        """
        returns list of instances from a json file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in json_list]
                return instances
        except FileNotFoundError:
            return []


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        A list of instances is serialized to a csv file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fields = ["id", "size", "x", "y"]
            else:
                return
            writer.writerow(fields)
            for obj in list_objs:
                writer.writerow([getattr(obj, field) for field in fields])


    @classmethod
    def load_from_file_csv(cls):
        """
        A list of instances are deserislized from a csv file
        """
        filename = cls.__name__ + ".csv"
        try:
            instances = []
            with open(filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    dictionary = {key: int(value) for key, value in row.items()}
                    instance = cls.create(**dictionary)
                    instances.append(instance)
            return instances
        except FileNotFoundError:
            return []
