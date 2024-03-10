#!/usr/bin/env python3
"""This is a module for file storage class.
The class is used to serializes instances to a JSON file
and deserializes JSON file to instances"""


import json

class FileStroage:
    """This class is used to serializes instances to a JSON
    file and deserializes JSON file to instances"""


    __file_path = ""
    __objects = {'objects': []}

    """
Public instance methods:
1. all(self): returns the dictionary __objects
2. new(self, obj): sets in __objects the obj with key <obj class name>.id
3. save(self): serializes __objects to the JSON file (path: __file_path)
4. reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
    """
    def all(self):
        """This method returns all the dictionary data in __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This method sets in an object in __objects
        with the key <obj class name>.id

        Args:
            obj - this argument is the object (new object) that
            is to be stored in __objects
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        data = {key: obj}
        FileStorage.__objects['objects'].append(data)

    def save(self):
        """This method serializes the objects in __objects to the JSON
        format and save them in the file, specified by __file_path"""
        with open(FileStorage.__file_path, 'w', encoding='utf8') as f:
            for obj in FileStorage.__objects['objects']:
                json.dump(obj, f, indent='')
