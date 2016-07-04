
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, Column, Integer, String, DateTime

import settings

DeclarativeBase = declarative_base()

def db_connect():
	"""
	performs database connection using database settings from settings.py
	returns sqlalchemy engine instance
	"""
	return create_engine(URL(**settings.DATABASE))

def create_cars_table(engine):
	DeclarativeBase.metadata.create_all(engine)
	
class Cars(DeclarativeBase):
	"""Sqlalchemy Cars model"""
	__tablename__ = "usedcars"
	
	id = Column(Integer, primary_key=True)
	Make = Column('make',String)
	Model = Column('model',String)
	TitleLocation = Column('titlelocation',String)
	Year = Column('year', String, nullable=True)
	Price = Column('price', String, nullable=True)