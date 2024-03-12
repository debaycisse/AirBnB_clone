#!/usr/bin/env python3
"""The module for defining user class"""

import sys
import os

sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
except Exception as e:
    print(e)


class User(BaseModel):
    """This is the user class definition"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()
        else:
            super().__init__(**kwargs)
