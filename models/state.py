#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    if storage_type == 'db':

        cities = relationship(
            "City",
            cascade="all, delete",
            backref="state"
        )
    else:
        @property
        def cities(self):
            """ Getter attribute to retrieve cities associated with this state """
            from models import storage

            city_instances = storage.all(City)  # Assuming 'City' is your City class
            return [city for city in city_instances.values() if city.state_id == self.id]