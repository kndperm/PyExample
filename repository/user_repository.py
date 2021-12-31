import sqlite3
from model.user import User


def add_user(user: User):
    connection = sqlite3.connect("pyTest.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO users VALUES {user.name} {user.password} {user.email}")
    connection.commit()
    connection.close()


# TODO write normal sql query
def upgrade_user(user: User):
    connection = sqlite3.connect("pyTest.db")
    cursor = connection.cursor()
    cursor.execute(f"UPDATE users SET NAME={user.name} WHERE id={user.id}")
    connection.commit()
    connection.close()


def delete_user(user_id: int):
    connection = sqlite3.connect("pyTest.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE from users WHERE ID = {user_id}")
    connection.commit()
    connection.close()


def select_user(user_id: int):
    connection = sqlite3.connect("pyTest.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE ID = {user_id}")
    connection.commit()
    connection.close()
    return cursor


def select_all():
    connection = sqlite3.connect("pyTest.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users")
    connection.commit()
    connection.close()
    return cursor


# def end_connection():
#     connection.commit()
#     connection.close()
