#!/usr/bin/python3
"""Class user"""

from models.base_model import BaseModel


class City(BaseModel):
    """class User that inherits from BaseModel"""
    state_id = ""
    name = ""
