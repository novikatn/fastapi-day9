from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.database import User
from app.models.engine import db_session
from app.schema.post import PostCreate, PostRead
from app.services.auth_service import get_current_user
from app.services.post_service import create_post, get_post, get_posts

posts_router = APIRouter(prefix="/posts", tags=["Posts"], dependencies=[Depends(get_current_user)])

# Get all posts
@posts_router.get("/", response_model=list[PostRead])
def get_posts_api(db: Session = Depends(db_session), user: User = Depends(get_current_user)):
  return get_posts(db, user)

# Get post by id
@posts_router.get("/{post_id}", response_model=PostRead)
def get_post_api(post_id: str, db: Session = Depends(db_session)):
  return get_post(db, post_id)

# Create Post
@posts_router.post("/", response_model=PostRead)
def create_post_api(post: PostCreate, db: Session = Depends(db_session), user: User = Depends(get_current_user)):
  return create_post(db, post, user)
