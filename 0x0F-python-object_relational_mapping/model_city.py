#!/usr/bin/python3
"""
This script defines a class City for use with SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    """
    Class City WITH ATTRIBUTES for the city table.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
