import sqlite3
from sqlalchemy import create_engine

# connection = sqlite3.connect()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def create_engine():
    return create_engine("sqlite://pyTest.db")


def get_sessionlocal():
    return sessionmaker(autocommit=False, autoflush=False, bind=create_engine())


def get_base():
    return declarative_base()
