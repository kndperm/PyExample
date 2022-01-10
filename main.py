from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from dto import user_dto
from dto.user_dto import UserCreate
from repository.database import SessionLocal
from service import user_service

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users/{id}", response_model=user_dto.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user(user_id, db)


@app.get("/users/", response_model=list[user_dto.User])
async def get_all_users(db: Session = Depends(get_db)):
    return user_service.get_all_user(db)


@app.post("/users/add/", response_model=user_dto.UserCreate)
async def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.add_user(user, db)


@app.put("/users/edit/{user_id}")
async def edit_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return user_service.update_user(user_id, user, db)


@app.delete("/users/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_user(user_id, db)
    return user_id
