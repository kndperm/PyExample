from dto import user_dto
from model.user import User
from sqlalchemy.orm import Session


def select_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def select_all(db: Session):
    return db.query(User).all()


def add_user(user: user_dto.UserCreate, db: Session):
    db_user = User(name=user.name, password=user.password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(user_id: int, user: user_dto.UserCreate, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if user.name:
        db_user.name = user.name
    if user.password:
        db_user.password = user.password
    if user.email:
        db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
