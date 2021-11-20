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


class UserModel(BaseModel):
    name: str
    username: str
    password: str
    access: bool

    class Config:
        schema_extra = {
            "example": {
                "name": "laura",
                "username": "drmamapa@hotmail.com",
                "password": "Senha.1500",
                "access": False
            }
        }


class UserResponseModel(BaseModel):
    data: dict

    class Config:
        schema_extra = {
            "example": {
                "data": {"message": "Exitoso"}
            }
        }


class ClientCreate(BaseModel):
    empresa: str
    placa_empresa: str
    placa: str
    bimensual: str
    soat: str
    tecnomecanica: str
    poliza: str
    bimensual: str
    archivo: str
    archivo2: str
    fecha_registro: str
    aprobado: str

    class Config:
        schema_extra = {
            "example": {
                "empresa": "jeltes",
                "placa_empresa": "HHH",
                "placa": "SDF453",
                "bimensual": "11/5/2002",
                "soat": "12/7/2002",
                "tecnomecanica": "10/10/2021",
                "poliza": "10/1/2021",
                "bimensual": "11/8/2021",
                "archivo": "",
                "archivo2": "",
                "fecha_registro": "10/8/2020",
                "aprobado": "True",
            }
        }
