#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Integer,
    Float
    )
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(
        String(60),
        ForeignKey('cities.id', ondelete="CASCADE"),
        nullable=False)
    user_id = Column(
        String(60),
        ForeignKey('users.id', ondelete="CASCADE"),
        nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if storage_type == 'db':

        reviews = relationship(
            "Review",
            cascade="all, delete",
            backref="place"
        )
    else:
        @property
        def reviews(self):
            """ Getter attribute to retrieve cities associated with this state """
            from models import storage

            reviews = storage.all(Place)
            return [review for review in reviews.values() if review.place_id == self.id]
