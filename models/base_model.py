#!/usr/bin/env python3
"""
this is the uuid module in python it is used for the creation of unique id.
this is date and time module in python it helps us work with time.
"""
from datetime import datetime
from uuid import uuid4
# import models


class BaseModel():
    """Base model class, this is the super class
    where every other class would inherit from

    """
    id = ""
    created_at = ""
    updated_at = ""
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self):
        """Initialize a new instance of BaseModel.
        Args:
            - *args: it's not used
            - **kwargs: it's a dictionary of key-values arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns the string representation of instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """helps save every created instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """helps convert object to dictionary"""
        model_data = self.__dict__.copy()
        model_data['__class__'] = self.__class__.__name__
        model_data['created_at'] = self.created_at.isoformat()
        model_data['updated_at'] = self.updated_at.isoformat()
        return model_data
