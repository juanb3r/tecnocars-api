from process.db_queries import UserQuery, ClientQuery
from process.utils import hash_md5_utils
import os
import pathlib

user_query = UserQuery()
client_query = ClientQuery()


def create_user_process(user):
    user.password = hash_md5_utils(user.password)
    return user_query.new_user_tb(user)


def user_login_process(user):
    user.password = hash_md5_utils(user.password)
    return user_query.get_user_login_tb(user.username, user.password)


def create_client_process(client):
    return client_query.new_client_tb(client)


def upload_file_process(file):

    try:
        route = "carpeta"
        os.mkdir("carpeta")
        f = open(route+"/prueba.jpg", "wb")
        f.write(file)
        f.close()
        return {"data": {"message": "Archivo subido"}}
    except Exception as error:
        return {"data": {"erorr": f"{error}"}}
