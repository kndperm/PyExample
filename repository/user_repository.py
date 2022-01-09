from dto import user_dto
from model.user import User
from sqlalchemy.orm import Session


def select_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def select_all(db: Session):
    return db.query(User).all()


def add_user(user: user_dto.User, db: Session):
    db_user = User(name=user.name, password=user.password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# TODO write normal sql query
def upgrade_user(user_id: int, user: user_dto.User, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user.name
    db_user.password = user.password
    db_user.email = user.email
    db.commit()


def delete_user(user_id: int, db: Session):
    user = db.query(User).first(User.id == user_id)
    db.delete(user)
    db.commit()
