#!/usr/bin/env python3
"""The module for defining user class"""
import sys
import os
sys.path.append(os.getcwd())
from models.base_model import BaseModel

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

        
if '__main__' == __name__:
    a = User()
    a.first_name = "Betty"
    a.last_name = "Bar"
    a.email = "airbnb@mail.com"
    a.password = "root"
    a.save()
    print(a.to_dict())