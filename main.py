from fastapi import FastAPI
from dto.user_dto import User
from repository import database
from service import user_service

app = FastAPI()


def get_db():
    db = database.get_sessionlocal()
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


@app.get("/users/{id}")
async def get_user(user_id: int):
    return user_service.get_user(user_id, get_db())


@app.get("/users/")
async def get_all_users():
    return user_service.select_all(get_db())


@app.post("/users/add/")
async def add_user(user: User):
    user_service.add_user(user, get_db())
    return {"message": "User Added",
            "User": user}


# TODO ???
@app.put("/users/edit/{user_id}")
async def edit_user(user_id: int, user: User):
    user_service.upgrade_user(user_id, user, get_db())
    return user


@app.delete("/users/delete/{user_id}")
async def delete_user(user_id: int):
    user_service.delete_user(user_id, get_db())
    return user_id
