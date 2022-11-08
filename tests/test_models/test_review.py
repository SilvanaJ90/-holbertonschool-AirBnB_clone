#!/usr/bin/python3
"""Test user"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """class Test from user"""

    def test_review(self):
        """Test User"""
        r = Review()
        self.assertTrue(issubclass(r.__class__, BaseModel))
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")


        r.place_id = "My First Model"
        r.user_id = "My First Model"
        r.text = "My First Model"
        s = f"[{r.__class__.__name__}] ({r.id}) {r.__dict__}"
        self.assertEqual(s, str(r))


if __name__ == '__main__':
    unittest.main()
