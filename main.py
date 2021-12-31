from fastapi import FastAPI
from model.user import User
from repository import user_repository

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/users/{id}")
async def get_user(user_id: int):
    return user_repository.select_user(user_id)


@app.get("/users/")
async def get_all_users():
    return user_repository.select_all()


@app.post("/users/add/")
async def add_user(user: User):
    user_repository.add_user(user)
    return user


# TODO ???
@app.put("/users/edit/{user_id}")
async def edit_user(user_id: int, user: User):
    user_repository.upgrade_user(user)
    return user


@app.delete("/users/delete/{user_id}")
async def delete_user(user_id: int):
    user_repository.delete_user(user_id)
    return user_id
