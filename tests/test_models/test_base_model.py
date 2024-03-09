#!/usr/bin/env python3
""" This module houses a set of test cases for the BaseModel class"""


import os
import sys
import unittest
from datetime import datetime


sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
except Exception as e:
    print(e)


class TestBaseModel(unittest.TestCase):
    """This test class collects a series of tests for the class BaseModel"""

    def test_init_method(self):
        """This method tests the attribute of an
        instance of BaseModel class"""
        bm = BaseModel()
        self.assertTrue(len(bm.id) > 0 and isinstance(bm.id, str))
        self.assertTrue(isinstance(bm.created_at, datetime))
        self.assertTrue(isinstance(bm.updated_at, datetime))

    def test_str_method(self):
        """This method test the str magic function"""
        bm = BaseModel()
        bm_str = str(bm)
        bm_expected_str = "[{}] ({}) {}".format(bm.__class__.__name__,
                                                bm.id, bm.__dict__)
        self.assertEqual(bm_str, bm_expected_str)

    def test_save_method(self):
        """This method tests the value of the attribute
        that is updated by the save method"""
        bm = BaseModel()
        updated_at_before = bm.updated_at
        bm.save()
        self.assertNotEqual(updated_at_before, bm.updated_at)
        self.assertTrue(isinstance(bm.updated_at, datetime))
        self.assertTrue(isinstance(updated_at_before, datetime))

    def test_to_dict_method(self):
        """This method validates the logic of the
        to_dict method via testing"""
        bm = BaseModel()
        self.assertFalse("__class__" in bm.__dict__)
        bm_dict = bm.to_dict()
        self.assertTrue("__class__" in bm_dict)
