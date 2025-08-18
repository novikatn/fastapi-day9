from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.core.settings import settings
from app.routes.auth_route import auth_router
from app.routes.post_route import posts_router
from app.routes.user_route import users_router
from app.schema.user import UserRead

app = FastAPI(
    title=settings.APP_NAME, docs_url=settings.DOCS_URL, redoc_url=settings.REDOC_URL, openapi_url=settings.OPENAPI_URL
)

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(posts_router)


@app.get("/")
def read_root():
    # send_email.delay("novikatn@gmail.com", "Test", "Content")
    return {"message": "it works! After CI/CD"}


@app.get("/scalar", response_model=list[UserRead])
def get_scalar():
    return get_scalar_api_reference(title=settings.APP_NAME, openapi_url=settings.OPENAPI_URL)
