from sqlalchemy import Column, Integer, String

from repository.database import get_base


class User(get_base()):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
