#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
import models

class DBStorage:
    """This class manages storage of hbnb models in a database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage"""
        '''dialect[+driver]://user:password@host/dbname[?key=value..]'''
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV", "none")
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{pwd}@{host}/{db}", pool_pre_ping=True)
        if env == "test":
            # drop all tables
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        '''
            Query current database session
        '''
        db_dict = {}

        if cls != "":
            objs = self.__session.query(models.classes[cls]).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                db_dict[key] = obj
            return db_dict

        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if len(objs) > 0:
                        for obj in objs:
                            key = "{}.{}".format(obj.__class__.__name__,
                                                 obj.id)
                            db_dict[key] = obj
            return db_dict

    def new(self, obj):
        '''
            Add object to current database session
        '''
        self.__session.add(obj)

    def save(self):
        '''
            Commit all changes of current database session
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
            Delete from current database session
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
            Commit all changes of current database session
        '''
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

        
