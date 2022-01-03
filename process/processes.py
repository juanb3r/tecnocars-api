from process.db_queries import UserQuery, ClientQuery
from process.utils import hash_md5_util, create_path_util


user_query = UserQuery()
client_query = ClientQuery()


def create_user_process(user):
    user.password = hash_md5_util(user.password)
    return user_query.new_user(user)


def user_login_process(user):
    user.password = hash_md5_util(user.password)
    return user_query.get_user_login(user.username, user.password)


def upload_file_process(preventive_review, corrective_sheet, date_id_register):
    try:
        create_path_util(
            preventive_review, corrective_sheet, date_id_register)
        client_query.edit_client_path_file(date_id_register)
        return {"data": {"message": "Archivos subidos exitosamente"}}

    except Exception:
        return {"data": {"message": "Error al subir los archivos"}}


def create_client_process(client):
    return client_query.new_client(client)


def edit_client_process(client, number_id):
    return client_query.edit_client(client, number_id)


def delete_client_process(delete_id):
    return client_query.delete_client(delete_id)


def show_client_process():
    return client_query.show_clients()
