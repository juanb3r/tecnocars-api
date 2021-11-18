import hashlib
import json

from process.db_queries import UserQuery


user_query = UserQuery()


def create_user_process(user):
    hashed_password = hashlib.md5(user.password.encode())
    user.password = hashed_password.hexdigest()
    return user_query.new_user_tb(user)


def user_login_process(user):
    hashed_password = hashlib.md5((user.password).encode())
    user.password = hashed_password.hexdigest()
    return user_query.get_user_login_tb(user.username, user.password)
