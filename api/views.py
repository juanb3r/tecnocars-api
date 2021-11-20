import logging
from fastapi import APIRouter
from process.handlers import create_user_handler, user_login_handler

from process.serializers import ClientCreate, UserLoginModel, UserModel,\
    UserResponseModel


router = APIRouter()
logger = logging.getLogger("router")


@router.get("/")
async def root():
    """
    Verificar que la app esta muncionando

    Returns:
        [dict]: Hello World
    """
    return {"message": "Hello World"}


@router.post("/user", tags=["user"], response_model=UserResponseModel)
async def login_user(user: UserLoginModel) -> dict:
    """
    El usuario debe loguearse en la app,
    ingresando su usuario y contraseña para ingresar

    Args:
        user (UserLoginModel): 1) username: str    2) password: str

    Returns:
        dict:
            Respuesta de la petición 1) datos del usuario
            o 2) verificar datos, correo o clave erronea

    """
    return user_login_handler(user)


@router.post("/create-user", tags=["user"])
async def create_user(user: UserModel) -> dict:
    """
    Creacion del usurio con sus datos nombre, correo, clave

    Args:
        user (UserModel): 1) name: str  2) username: str
            3) password: str    4) access: bool

    Returns:
        dict:
            Respuesta de la petición 1) usuario creado, 2)
                usuario existente, 3) correo no valido
    """
    return create_user_handler(user)


@router.post("/client", tags=["client"])
async def login_client(client: ClientCreate):
    return {"client": client}
