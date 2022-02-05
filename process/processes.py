from process.db_queries import UserQuery, ClientQuery
from process.utils import SessionManager, hash_md5_util, create_path_util


user_query = UserQuery()
client_query = ClientQuery()
session_manager = SessionManager()

start_message = "Usuario no ha iniciado sesión"
message_access = "El usuario no puede hacer esta acción"


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
        if session_manager.user.access:
            user.password = hash_md5_util(user.password)
            return user_query.new_user(user)
        else:
            return {"data": {"message": message_access}}
    else:
        return {"data": {"message": start_message}}


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
        session_manager.value = session_login["data"]["value"]
        session_manager.user = session_login["data"]["user"]
        return {"data": {"message": "Sesión iniciada"}}
    else:
        return {"data": {"message": "el usuario ya ha iniciado sesión"}}


def edit_user_process(user, number_id):
    if session_manager.value:
        if session_manager.user.access:
            return user_query.edit_user(user, number_id)
        else:
            return {"data": {"message": message_access}}
    else:
        return {"data": {"message": start_message}}


def delete_user_process(delete_id):
    if session_manager.value:
        if session_manager.user.access:
            return user_query.delete_user(delete_id)
        else:
            return {"data": {"message": message_access}}
    else:
        return {"data": {"message": start_message}}


def show_user_process():
    if session_manager.value:
        if session_manager.user.access:
            return user_query.show_users()
        else:
            return {"data": {"message": message_access}}
    else:
        return {"data": {"message": start_message}}


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
        if session_manager.user.access:
            return client_query.new_client(client)
        else:
            return {"data": {"message": message_access}}
    else:
        return {"data": {"message": start_message}}


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
        if session_manager.user.access:
            return client_query.edit_client(client, number_id)
        else:
            return {"data": {"message": message_access}}
    else:
        return {"data": {"message": start_message}}


def delete_client_process(delete_id):
    if session_manager.value:
        if session_manager.user.access:
            return client_query.delete_client(delete_id)
        else:
            return {"data": {"message": message_access}}
    else:
        return {"data": {"message": start_message}}


def show_client_process():
    if session_manager.value:
        if session_manager.user.access:
            return client_query.show_clients()
        else:
            return {"data": {"message": message_access}}
    else:
        return {"data": {"message": start_message}}


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
        return {"data": {"message": "Sesión cerrada"}}
    else:
        return {"data": {"message": start_message}}


def upload_file_process(preventive_review, corrective_sheet, date_id_register):
    if session_manager.value:
        if session_manager.user.access:
            try:
                create_path_util(
                    preventive_review, corrective_sheet, date_id_register)
                client_query.edit_client_path_file(date_id_register)
                return {"data": {"message": "Archivos subidos exitosamente"}}

            except Exception:
                return {"data": {"message": "Error al subir los archivos"}}
        else:
            return {"data": {"message": message_access}}
    else:
        return {"data": {"message": start_message}}
