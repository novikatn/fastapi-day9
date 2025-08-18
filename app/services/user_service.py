from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.models.database import User
from app.schema.auth import RegisterResponse


def create_user(db_session: Session, user: RegisterResponse):
    new_user = User(**user.model_dump())
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user


def get_user(db_session: Session, user_id: str):
    # Lazy load query
    # statement = select(User).where(User.id == user_id)
    # user = db_session.exec(statement).first()

    # _ = user.posts
    # return user
    statement = select(User).options(selectinload(User.posts)).where(User.id == user_id)
    return db_session.exec(statement).first()


def get_users(db_session: Session):
    return db_session.exec(select(User)).all()
