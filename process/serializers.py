from pydantic import BaseModel
from typing import Optional


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "Foo",
                "password": "Senha.1500",
            }
        }
