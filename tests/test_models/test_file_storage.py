#!/usr/bin/env python3
""" This module houses a set of test cases for the FileStorage class"""


import os
import sys
import unittest
from datetime import datetime


sys.path.append(os.getcwd())
try:
    from models.base_model import BaseModel
    from models.engine.file_storage import FileStorage
except Exception as e:
    print(e)


class TestFileStorage(unittest.TestCase):
    """This test class collects a series of tests for the FileStorage class"""

    def setUp(self):
        """This sets up the environment for each test case"""
        FileStorage.reset_objects()

    def test_all_method_of_file_storage(self):
        """This method tests that the all method returns an empty
        dictionary when no model is created"""
        f = FileStorage()
        self.assertTrue(len(f.all()) == 0)

    def test_all_method_returned_data(self):
        """This test the returned datatype of the all method"""
        f = FileStorage()
        self.assertIsInstance(f.all(), dict)

    def test_all_method_of_file_storage2(self):
        """This tests that the all method returns a value when there
        is at least one model in existence"""
        b = BaseModel()
        f = FileStorage()
        self.assertTrue(len(f.all()) > 0)

    def test_new_method(self):
        """This method tests that the new method adds a given
        object to the available objects"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel()
        f = FileStorage()
        self.assertEqual(len(f.all()), 3)
