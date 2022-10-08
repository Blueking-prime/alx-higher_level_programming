#!/usr/bin/python3
'''state class'''
from model_city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''
    A state

    Instance attributes:
        id (int) - State ID
        name (str) - Name of state
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates='state')
