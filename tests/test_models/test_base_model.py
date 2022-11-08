#!/usr/bin/python3
"""
Test BaseModel
"""


from models.base_model import BaseModel
import unittest


class TestsBaseModel(unittest.TestCase):
    """ Test BaseModel """
    def testBaseMdlSave(self):
        myModel = BaseModel()
        dt = myModel.updated_at
        dt.save()
        myModel2 = dt.update_at
        self.assertNotEqual(myModel, myModel2)
