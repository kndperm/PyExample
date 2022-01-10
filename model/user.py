from sqlalchemy import Column, Integer, String

from repository.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
