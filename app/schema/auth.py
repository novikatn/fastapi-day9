from pydantic import BaseModel


class AuthRegister(BaseModel):
    full_name: str
    email: str
    password: str

class AuthLogin(BaseModel):
    email: str
    password: str

