import logging
from fastapi import APIRouter
from process.handlers import create_user_handler, user_login_handler

from process.serializers import ClientCreate, UserLoginModel, UserModel


router = APIRouter()
logger = logging.getLogger("router")


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/user", tags=["user"])
async def login_user(user: UserLoginModel):
    return user_login_handler(user)


@router.post("/create-user", tags=["user"])
async def create_user(user: UserModel):
    return create_user_handler(user)


@router.post("/client", tags=["client"])
async def login_client(client: ClientCreate):
    return {"client": client}
