#!/usr/bin/python3
"""Test user"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """class Test from user"""

    def test_state(self):
        """Test User"""
        stt = State()
        self.assertTrue(issubclass(stt.__class__, BaseModel))
        self.assertTrue(hasattr(stt, "id"))
        self.assertTrue(hasattr(stt, "created_at"))
        self.assertTrue(hasattr(stt, "updated_at"))
        self.assertEqual(stt.name, "")

        stt.name = "My First Model"
        s = f"[{stt.__class__.__name__}] ({stt.id}) {stt.__dict__}"
        self.assertEqual(s, str(stt))


if __name__ == '__main__':
    unittest.main()
