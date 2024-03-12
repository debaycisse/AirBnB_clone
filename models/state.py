#!/usr/bin/env python3
"""This module contains the state class definition"""


from base_model import BaseModel

class State(BaseModel):
    """This is the class for State object"""
    name = ""
    
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()
        else:
            super().__init__(**kwargs)