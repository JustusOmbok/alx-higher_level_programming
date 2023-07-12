#!/usr/bin/python3

def class_to_json(obj):
    """A dictionar, string, or integer description is returned
    """
    attributes = obj.__dict__
    return {key: attributes[key] for key in attributes if not callable(attributes[key])}
