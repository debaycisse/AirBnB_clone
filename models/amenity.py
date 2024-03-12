#!/usr/bin/env python3
"""This module contains the Amenity class definition"""


from base_model import BaseModel


class Amenity(BaseModel):
    """This is the class for Amenity object"""

    name = ""

    def __init__(self, *args, **kwargs):
        """This method initializes an instance of this class"""
        if len(kwargs) == 0:
            super().__init__()
        else:
            super().__init__(**kwargs)
