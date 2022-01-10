from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    password: str
    email: str

    class Config:
        orm_mode = True


class User(UserCreate):
    id: int
