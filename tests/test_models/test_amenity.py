#!/usr/bin/python3
"""Test user"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """class Test from user"""

    def test_amenity(self):
        """Test User"""
        a = Amenity()
        self.assertTrue(issubclass(a.__class__, BaseModel))
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertEqual(a.name, "")

        a.name = "My First Model"
        s = f"[{a.__class__.__name__}] ({a.id}) {a.__dict__}"
        self.assertEqual(s, str(a))


if __name__ == '__main__':
    unittest.main()
