# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(VARCHAR(254), primary_key=True, nullable=False)
    password = Column(String(254))
    numOfDevices = Column(Integer)
