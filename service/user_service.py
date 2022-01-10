from sqlalchemy.orm import Session

from dto.user_dto import UserCreate
from repository import user_repository


def get_user(user_id: int, db: Session):
    return user_repository.select_user(user_id, db)


def get_all_user(db: Session):
    return user_repository.select_all(db)


def add_user(user: UserCreate, db: Session):
    return user_repository.add_user(user, db)


def update_user(user_id: int, user: UserCreate, db: Session):
    return user_repository.update_user(user_id, user, db)


def delete_user(user_id: int, db: Session):
    user_repository.delete_user(user_id, db)
