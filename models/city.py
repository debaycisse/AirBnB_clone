#!/usr/bin/env python3
"""This module contains the city class definition"""


from base_model import BaseModel

class City(BaseModel):
    """This is the class for City object"""
    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()
        else:
            super().__init__(**kwargs)