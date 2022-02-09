from process.db_queries import UserQuery, ClientQuery
from process.utils import SessionManager, hash_md5_util, create_path_util
from process.constants import (
    CURRENTLY_LOGGED,
    FORBIDDEN,
    LOGGED,
    LOGGED_OUT,
    NOT_LOGGED
)


user_query = UserQuery()
client_query = ClientQuery()
session_manager = SessionManager()


def create_user_process(user):
    """
    Creacion del usurio con sus datos nombre, correo, clave, access

    Args:
        user (dict):
            1. name: str
            2. username: str
            3. password: str
            4. access: bool

    Returns:
        [dict]:  {"data": {"message": }}
            1. Respueta return
            2. Usuario no ha iniciado sesión
            3. El usuario no puede hacer esta acción
    """
    if session_manager.value:
        if session_manager.user["access"]:
            user.password = hash_md5_util(user.password)
            response = user_query.new_user(user)
            return response
        return {
            "data": {},
            "message": FORBIDDEN,
            "status": 401
        }
    return {
        "data": {},
        "message": NOT_LOGGED,
        "status": 401
    }


def user_login_process(user):
    """
    Realizamos el hash de la contraseña usando md5,
    realizamos la consulta del usuario

    Args:
        user (dict): Contraseña y usuario

    Returns:
        [dict]:
        {data: {message: Sesión iniciada ó el usuario ya ha iniciado sesión}}
    """
    if not session_manager.value:
        user.password = hash_md5_util(user.password)
        session_login: dict = user_query.get_user_login(
            user.username, user.password
        )
        if session_login["data"].get("error"):
            return {
                "data": session_login["data"],
                "message": session_login["message"],
                "status": 500
            }
        else:
            session_manager.value = session_login["data"]["value"]
            session_manager.user = session_login["data"]["user"]
        return {
            "data": session_manager.user,
            "message": LOGGED,
            "status": 200
        }
    return {
            "data": session_manager.user,
            "message": CURRENTLY_LOGGED,
            "status": 200
        }


def edit_user_process(user, number_id):
    if session_manager.value:
        if session_manager.user["access"]:
            response = user_query.edit_user(user, number_id)
            return response

        return {
            "data": {},
            "message": FORBIDDEN,
            "status": 401
        }
    return {
        "data": {},
        "message": NOT_LOGGED,
        "status": 401
    }


def delete_user_process(delete_id):
    if session_manager.value:
        if session_manager.user["access"]:
            return user_query.delete_user(delete_id)
        return {
            "data": {},
            "message": FORBIDDEN,
            "status": 401
        }
    return {
        "data": {},
        "message": NOT_LOGGED,
        "status": 401
    }


def show_user_process():
    if session_manager.value:
        if session_manager.user["access"]:
            response = user_query.show_users()
            return response
        return {
            "data": {},
            "message": FORBIDDEN,
            "status": 401
        }
    return {
        "data": {},
        "message": NOT_LOGGED,
        "status": 401
    }


def create_client_process(client):
    """
    Creacion de un cliente

    Args:
        client (dict):
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
        [dict]: {"data": {"message": }}
            1. Usuario no ha iniciado sesión
            2. El usuario no puede hacer esta acción
            3. El cliente fue creado
            4. Error
    """
    if session_manager.value:
        if session_manager.user["access"]:
            response = client_query.new_client(client)
            return response
        return {
            "data": {},
            "message": FORBIDDEN,
            "status": 401
        }
    return {
        "data": {},
        "message": NOT_LOGGED,
        "status": 401
    }


def edit_client_process(client, number_id):
    """
    Editamos el cliente con los parametros
    Args:
        client (dict):
        number_id (int):
    Returns:
        [type]: {"data": {"message": }}
            1. El usuario fue editado
            2. Erorr
            3. Usuario no ha iniciado sesión
            4. El usuario no puede hacer esta acción

    """
    if session_manager.value:
        if session_manager.user["access"]:
            response = client_query.edit_client(client, number_id)
            return response
        return {
            "data": {},
            "message": LOGGED_OUT,
            "status": 200
        }
    return {
        "data": {},
        "message": NOT_LOGGED,
        "status": 401
    }


def delete_client_process(delete_id):
    if session_manager.value:
        if session_manager.user["access"]:
            response = client_query.delete_client(delete_id)
            return response
        return {
            "data": {},
            "message": FORBIDDEN,
            "status": 401
        }
    return {
        "data": {},
        "message": NOT_LOGGED,
        "status": 401
    }


def show_client_process():
    if session_manager.value:
        if session_manager.user["access"]:
            response = client_query.show_clients()
            return response
        response = client_query.show_client(session_manager.user["name"])
        return response
        # return {
        #     "data": {},
        #     "message": FORBIDDEN,
        #     "status": 401
        # }
    return {
        "data": {},
        "message": NOT_LOGGED,
        "status": 401
    }


def user_close_session_process():
    """
    Cierre de sesión

    Returns:
        [type]:
        {"data": {"message": Sesión cerrada ó Usuario no ha iniciado sesión}}}
    """
    if session_manager.value:
        session_manager.value = False
        session_manager.user = {}
        return {
            "data": {},
            "message": LOGGED_OUT,
            "status": 200
        }
    return {
        "data": {},
        "message": NOT_LOGGED,
        "status": 401
    }


def upload_file_process(preventive_review, corrective_sheet, date_id_register):
    if session_manager.value:
        if session_manager.user["access"]:
            try:
                create_path_util(
                    preventive_review, corrective_sheet, date_id_register)
                client_query.edit_client_path_file(date_id_register)
                return {
                    "data": {},
                    "message": "Archivos subidos exitosamente",
                    "status": 200
                }

            except Exception:
                return {
                    "data": {},
                    "message": "Error al subir los archivos",
                    "status": 500
                }
        return {
            "data": {},
            "message": FORBIDDEN,
            "status": 401
        }
    return {
            "data": {},
            "message": NOT_LOGGED,
            "status": 401
        }
