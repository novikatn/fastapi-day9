from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from app.models.database import User
from app.models.engine import db_session
from app.schema.auth import AuthLogin, AuthRegister
from app.schema.user import UserRead
from app.services import auth_service

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(user: AuthRegister, db: Session = Depends(db_session)):
    try:
      user.password = auth_service.hash_password(user.password)
      new_user = User(**user.model_dump())
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      return new_user
    except IntegrityError:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered.")
    except Exception as e:
      raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@auth_router.post("/login")
def login(auth_login: AuthLogin, db: Session = Depends(db_session)):
    return
