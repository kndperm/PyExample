from pydantic import BaseModel


class User(BaseModel):
    name: str
    password: str
    email: str

    class Config:
        orm_mode = True
