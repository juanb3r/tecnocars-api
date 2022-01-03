from datetime import date
from pydantic import BaseModel


class UserLoginModel(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "drmamapa@hotmail.com",
                "password": "Senha.1500"
            }
        }


class UserCreateModel(BaseModel):
    name: str
    username: str
    password: str
    access: bool

    class Config:
        schema_extra = {
            "example": {
                "name": "Laura en America",
                "username": "drmamapa@hotmail.com",
                "password": "Senha.1500",
                "access": False
            }
        }


class ResponseModel(BaseModel):
    data: dict

    class Config:
        schema_extra = {
            "example": {
                "data": {"message": "Exitoso"}
            }
        }


class ClientCreateModel(BaseModel):
    empresa: str
    placa_empresa: str
    placa: str
    bimensual: date
    soat: date
    tecnomecanica: date
    poliza: date
    fecha_registro: date
    aprobado: bool

    class Config:
        schema_extra = {
            "example": {
                "empresa": "jeltes",
                "placa_empresa": "HHH",
                "placa": "SDF453",
                "bimensual": "2021-09-30",
                "soat": "2002-12-7",
                "tecnomecanica": "2021-10-10",
                "poliza": "2021-10-1",
                "fecha_registro": "2020-10-8",
                "aprobado": False
            }
        }
