import sqlite3
from sqlalchemy import create_engine

# connection = sqlite3.connect()
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Engine = create_engine("sqlite:///./pyTest.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)

Base = declarative_base()
