from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.models.database import Post, User
from app.schema.post import PostCreate


def create_post(db_session: Session, post: PostCreate, user):
    new_post = Post(**post.model_dump(), user_id=user.id)
    db_session.add(new_post)
    db_session.commit()
    db_session.refresh(new_post)
    return new_post


def get_post(db_session: Session, post_id: str):
    statement = select(Post).options(selectinload(Post.user)).where(Post.id == post_id)
    return db_session.exec(statement).first()


def get_posts(db_session: Session, user: User):
    # return db_session.exec(select(Post)).all()
    statement = select(Post).where(Post.user_id == user.id)
    return db_session.exec(statement).all()
