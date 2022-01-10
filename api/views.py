import logging
from fastapi import APIRouter
# from fastapi.datastructures import UploadFile
from fastapi.params import File, Form
from process.handlers import create_user_handler, user_login_handler,\
    create_client_handler, upload_file_handler, edit_client_handler,\
    delete_client_handler, show_client_handler, user_closed_session_handler

from process.serializers import ClientCreateModel, UserLoginModel,\
    UserCreateModel, ResponseModel


router = APIRouter()
logger = logging.getLogger("router")


@router.get("/")
async def root() -> dict:
    """
    Verificar que la app esta funcionando

    Returns:
        [dict]: Hello World
    """
    return {"message": "Hello World"}


@router.post("/user", tags=["user"], response_model=ResponseModel)
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


@router.post("/close-session", tags=["user"], response_model=ResponseModel)
async def close_session() -> dict:
    return user_closed_session_handler()


@router.post("/create-user", tags=["user"], response_model=ResponseModel)
async def create_user(user: UserCreateModel) -> dict:
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


@router.post("/create-client", tags=["client"], response_model=ResponseModel)
async def create_client(
        client: ClientCreateModel
                    ) -> dict:
    return create_client_handler(client)


@router.put("/edit-client", tags=["client"], response_model=ResponseModel)
async def edit_client(
    client: ClientCreateModel,
    number_id: int
) -> dict:
    return edit_client_handler(client, number_id)


@router.delete(
    "/delete-client/{delete_id}",
    tags=["client"],
    response_model=ResponseModel)
async def delete_client(delete_id: int) -> dict:
    return delete_client_handler(delete_id)


@router.get("/show-client", tags=["client"], response_model=ResponseModel)
async def show_client() -> dict:
    return show_client_handler()


@router.post("/create-upload", tags=["upload"], response_model=ResponseModel)
async def create_upload_file(
    preventive_review: bytes = File(...),
    corrective_sheet: bytes = File(...),
    date_id_register: str = Form(...)
        ) -> dict:
    return upload_file_handler(
        preventive_review,
        corrective_sheet,
        date_id_register)
