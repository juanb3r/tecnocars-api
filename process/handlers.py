from process.processes import create_user_process, user_login_process,\
    create_client_process, upload_file_process


def user_login_handler(user: object) -> dict:
    return user_login_process(user)


def create_user_handler(user: object) -> dict:
    return create_user_process(user)


def create_client_handler(client: object) -> dict:
    return create_client_process(client)


def upload_file_handler(file) -> dict:
    return upload_file_process(file)
