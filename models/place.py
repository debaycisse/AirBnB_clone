#!/usr/bin/env python3
"""This module contains the definition for amenity class"""

from base_model import BaseModel


class Amenity(BaseModel):
    """This is the class definition for the amenity object"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = 0.0
    longitude = 0.0
    amenity_id = []

    def __init__(self, *args, **kwargs):
        """This method initializes an object of this class"""
        if len(kwargs) == 0:
            super().__init__()
        elif len(kwargs) > 0:
            super().__init__(**kwargs)
