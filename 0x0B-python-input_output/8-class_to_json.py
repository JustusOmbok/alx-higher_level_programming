#!/usr/bin/python3

def class_to_json(obj):
    """A dictionar, string, or integer description is returned
    """
    attributes = obj.__dict__
    result = {}

    for key in attributtes:
        if not callable(attributes[key]):
            result[key] = attributes[key]

    return result
