import logging
from fastapi import APIRouter

from process.serializers import UserLogin

router = APIRouter()
logger = logging.getLogger("router")


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/user", tags=["user"])
async def login_user(user: UserLogin):
    return {"user": user}
