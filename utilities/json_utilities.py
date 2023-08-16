from typing import Any
import os, json


def get_object_from_file(json_file) -> Any:
    """Get the JSON object based on the JSON file"""
    json_obj = None
    with open(json_file) as data_file:
        json_obj = json.load(data_file)
    return json_obj