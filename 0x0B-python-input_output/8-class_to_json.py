#!/usr/bin/python3
"""
function that returns the dictionary description with simple data structure
"""
def class_to_json(obj):
    """A dictionar, string, or integer description is returned
    """
    return vars(obj)
