#!/usr/bin/python3
'''state class'''
from model_state import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class City(Base):
    '''
    A city

    Instance attributes:
        id (int) - State ID
        name (str) - Name of state
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship("State", back_populates='cities')
