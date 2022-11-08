#!/usr/bin/python3
"""Test user"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """class Test from user"""

    

    def test_place(self):
        """Test User"""
        p = Place()
        self.assertTrue(issubclass(p.__class__, BaseModel))
        self.assertTrue(hasattr(p, "id"))
        self.assertTrue(hasattr(p, "created_at"))
        self.assertTrue(hasattr(p, "updated_at"))
        self.assertEqual(p.city_id, "")
        self.assertEqual(p.user_id, "")
        self.assertEqual(p.name, "")
        self.assertEqual(p.description, "")
        self.assertEqual(p.number_rooms, 0)
        self.assertEqual(p.number_bathrooms, 0)
        self.assertEqual(p.max_guest, 0)
        self.assertEqual(p.price_by_night, 0)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertEqual(p.amenity_ids, {})

        p.city_id = "89"
        p.user_id = "1"
        p.name = "My First Model"
        p.description = "My First Model"
        p.number_rooms = 2
        p.number_bathrooms = 2
        p.max_guest = 3
        p.price_by_night = 20
        p.latitude = 5.5
        p.longitude = 3.2
        p.amenity_ids = {}
        s = f"[{p.__class__.__name__}] ({p.id}) {p.__dict__}"
        self.assertEqual(s, str(p))


if __name__ == '__main__':
    unittest.main()
