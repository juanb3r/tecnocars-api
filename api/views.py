import logging
from fastapi import APIRouter
from fastapi.params import File, Form
from fastapi.responses import JSONResponse
from process.handlers import create_user_handler, user_login_handler,\
    create_client_handler, upload_file_handler, edit_client_handler,\
    delete_client_handler, show_client_handler, user_closed_session_handler,\
    edit_user_handler, delete_user_handler, show_user_handler

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
            Respuesta de la petición 1) datos del usuario, inicio de sesión
            o 2) verificar datos, correo o clave erronea

    """
    response = user_login_handler(user)
    return JSONResponse(content=response, status_code=response.get("status"))


@router.post("/close-session", tags=["user"], response_model=ResponseModel)
async def close_session() -> dict:
    """
    Cerramos la sesión del usuario

    Returns:
        dict: {"data": {"message": }}
        1. Sesión cerrada
        2. Usuario no ha iniciado sesión
    """
    response = user_closed_session_handler()
    return JSONResponse(content=response, status_code=response.get("status"))


@router.post("/create-user", tags=["user"], response_model=ResponseModel)
async def create_user(user: UserCreateModel) -> dict:
    """
    Creacion del usurio con sus datos nombre, correo, clave, access

    Args:
        user (UserModel): 1) name: str  2) username: str
            3) password: str    4) access: bool

    Returns:
        dict: {"data": {"message": }}
            Respuesta de la petición
            1. El usuario fue creado
            2. El usuario ya existe
            3. Correo erroneo
            4. Usuario no ha iniciado sesión
            5. El usuario no puede hacer esta acción
            6. Error
    """
    response = create_user_handler(user)
    return JSONResponse(content=response, status_code=response.get("status"))


@router.put("/edit-user", tags=["user"], response_model=ResponseModel)
async def edit_user(
    user: UserCreateModel,
    number_id: int
) -> dict:
    """
    Tenemos el usuario editado y su id, de esta forma corregimos

    Args:
        user (UserCreateModel):
            {
            "name": str,
            "username": str,
            "password": str,
            "access": bool
            }
        number_id (int): id del usuario a editar

    Returns:
        dict: {"data": {"message": }}
            1. El usuario fue editado
            2. Usuario no ha iniciado sesión
            3. El usuario no puede hacer esta acción
    """
    response = edit_user_handler(user, number_id)
    return JSONResponse(content=response, status_code=response.get("status"))


@router.delete(
    "/delete-user/{delete_id}",
    tags=["user"],
    response_model=ResponseModel)
async def delete_user(delete_id: int) -> dict:
    """
    Recibimos el numero id del usuario a eliminar

    Args:
        delete_id (int): id del usuario a eliminar

    Returns:
        dict: {"data": {"message": }}
            1. El usuario fue borrado
            2. Error
            3. El usuario no puede hacer esta acción
            4. Usuario no ha iniciado sesión
    """
    return delete_user_handler(delete_id)


@router.get("/show-user", tags=["user"], response_model=ResponseModel)
async def show_user() -> dict:
    """
    Muestra todos los usuarios existentes en la base de datos

    Returns:
        dict: {"data": {"message": }}
            {
            "name": str,
            "username": str,
            "password": str,
            "access": bool
            }

    """
    response = show_user_handler()
    return JSONResponse(content=response, status_code=response.get("status"))


@router.post("/create-client", tags=["client"], response_model=ResponseModel)
async def create_client(
        client: ClientCreateModel
                    ) -> dict:
    """
    Creacion de un cliente con sus datos

    Args:
        client (ClientCreateModel):
            empresa: str
            placa_empresa: str
            placa: str
            bimensual: date
            soat: date
            tecnomecanica: date
            poliza: date
            fecha_registro: date
            aprobado: bool

    Returns:
        dict: {"data": {"message": }}
            1. Usuario no ha iniciado sesión
            2. El usuario no puede hacer esta acción
            3. El cliente fue creado
            4. Error
    """
    response = create_client_handler(client)
    return JSONResponse(content=response, status_code=response.get("status"))


@router.put("/edit-client", tags=["client"], response_model=ResponseModel)
async def edit_client(
    client: ClientCreateModel,
    number_id: int
) -> dict:
    """
    Tenemos el cliente editado y su id, de esta forma corregimos al cliente

    Args:
        client (ClientCreateModel):
            empresa: str
            placa_empresa: str
            placa: str
            bimensual: date
            soat: date
            tecnomecanica: date
            poliza: date
            fecha_registro: date
            aprobado: bool
        number_id (int): id del cliente a editar

    Returns:
        dict: {"data": {"message": }}
            1. El usuario fue editado
            2. Erorr
            3. Usuario no ha iniciado sesión
            4. El usuario no puede hacer esta acción
    """
    response = edit_client_handler(client, number_id)
    return JSONResponse(content=response, status_code=response.get("status"))


@router.delete(
    "/delete-client/{delete_id}",
    tags=["client"],
    response_model=ResponseModel)
async def delete_client(delete_id: int) -> dict:
    """
    Recibimos el numero id del cliente a eliminar

    Args:
        delete_id (int): id del cliente a eliminar

    Returns:
        dict: {"data": {"message": }}
            1. El cliente fue borrado
            2. Error
            3. El cliente no puede hacer esta acción
            4. Usuario no ha iniciado sesión
    """
    response = delete_client_handler(delete_id)
    return JSONResponse(content=response, status_code=response.get("status"))


@router.get("/show-client", tags=["client"], response_model=ResponseModel)
async def show_client() -> dict:
    """
    Muestra todos los clientes

    Returns:
        dict: {"data": {"message": }}
            empresa: str
            placa_empresa: str
            placa: str
            bimensual: date
            soat: date
            tecnomecanica: date
            poliza: date
            fecha_registro: date
            aprobado: bool
    """
    response = show_client_handler()
    return JSONResponse(content=response, status_code=response.get("status"))


@router.post("/create-upload", tags=["upload"], response_model=ResponseModel)
async def create_upload_file(
    preventive_review: bytes = File(...),
    corrective_sheet: bytes = File(...),
    date_id_register: str = Form(...)
        ) -> dict:
    """
    Recibimos los dos archivos a guardar y se organiza por empresa,
    placa del vehiculo y fecha
    Args:
        preventive_review (bytes, optional): Imagen. Defaults to File(...).
        corrective_sheet (bytes, optional): Imagen . Defaults to File(...).
        date_id_register (str, optional):
                1. empresa
                2. placa del vehiculo
                3. año, mes y día
                separado por _ (raya al piso)
                ejemplo: jelss_AAA753_2022_02_05
            . Defaults to Form(...).

    Returns:
        dict: {"data": {"message": }}
            1. Archivos subidos exitosamente
            2. Error al subir los archivos
            3. El cliente no puede hacer esta acción
            4. Usuario no ha iniciado sesión

    """
    response = upload_file_handler(
        preventive_review,
        corrective_sheet,
        date_id_register)
    return JSONResponse(content=response, status_code=response.get("status"))
