from fastapi import APIRouter, Depends

from sqlmodel import Session
from app.schema.auth import AuthRegister
from app.models.engine import db_session

auth_router = APIRouter()

@auth_router.post("/register")
def register(user: AuthRegister, db: Session = Depends(db_session))