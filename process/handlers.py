from process.processes import create_user_process, user_login_process


def user_login_handler(user: object) -> dict:
    return user_login_process(user)


def create_user_handler(user: object) -> dict:
    return create_user_process(user)
