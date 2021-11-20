from process.db_queries import UserQuery
from process.utils import hash_md5_utils


user_query = UserQuery()


def create_user_process(user):
    user.password = hash_md5_utils(user.password)
    return user_query.new_user_tb(user)


def user_login_process(user):
    user.password = hash_md5_utils(user.password)
    return user_query.get_user_login_tb(user.username, user.password)
