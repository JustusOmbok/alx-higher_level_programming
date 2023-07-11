#!/usr/bin/python3
"""
a pyrho data structure object rpresented by json
"""

import json

def from_json_string(my_obj):
    """
    returns a python object represented by json string
    """
    return json.loads(my_obj)
