from process.db_queries import UserQuery, ClientQuery
from process.utils import SessionManager, hash_md5_util, create_path_util


user_query = UserQuery()
client_query = ClientQuery()
session_manager = SessionManager()


def create_user_process(user):
    if session_manager.value:
        user.password = hash_md5_util(user.password)
        return user_query.new_user(user)
    else:
        return {"data": {"message": "Usuario no ha iniciado sesión"}}


def user_login_process(user):
#todo capturar diccinario y pasar al objecto
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


def user_close_session_process():
    if session_manager.value:
        session_manager.value = False
        session_manager.user = {}
        return {"data": {"message": "Sesión cerrada"}}
    else:
        return {"data": {"message": "Usuario no ha iniciado sesión"}}


def upload_file_process(preventive_review, corrective_sheet, date_id_register):
    if session_manager.value:
        try:
            create_path_util(
                preventive_review, corrective_sheet, date_id_register)
            client_query.edit_client_path_file(date_id_register)
            return {"data": {"message": "Archivos subidos exitosamente"}}

        except Exception:
            return {"data": {"message": "Error al subir los archivos"}}
    else:
        return {"data": {"message": "Usuario no ha iniciado sesión"}}


def create_client_process(client):
    if session_manager.value:
        return client_query.new_client(client)
    else:
        return {"data": {"message": "Usuario no ha iniciado sesión"}}


def edit_client_process(client, number_id):
    if session_manager.value:
        return client_query.edit_client(client, number_id)
    else:
        return {"data": {"message": "Usuario no ha iniciado sesión"}}


def delete_client_process(delete_id):
    if session_manager.value:
        return client_query.delete_client(delete_id)
    else:
        return {"data": {"message": "Usuario no ha iniciado sesión"}}


def show_client_process():
    if session_manager.value:
        return client_query.show_clients()
    else:
        return {"data": {"message": "Usuario no ha iniciado sesión"}}
