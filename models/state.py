#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete",
                          back_ref="state")

    @property
    def cities(self):
        """ Getter attribute to retrieve cities associated with this state """
        from models import storage, city

        city_instances = storage.all(city.City)  # Assuming 'City' is your City class
        return [city for city in city_instances.values() if city.state_id == self.id]