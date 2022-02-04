from process.processes import create_user_process, user_login_process,\
    create_client_process, upload_file_process, edit_client_process,\
    delete_client_process, show_client_process, user_close_session_process,\
    show_user_process, delete_user_process, edit_user_process


def user_login_handler(user: object) -> dict:
    return user_login_process(user)


def user_closed_session_handler() -> dict:
    return user_close_session_process()


def create_user_handler(user: object) -> dict:
    return create_user_process(user)


def edit_user_handler(user, number_id) -> dict:
    return edit_user_process(user, number_id)


def delete_user_handler(delete_id) -> dict:
    return delete_user_process(delete_id)


def show_user_handler() -> dict:
    return show_user_process()


def create_client_handler(client) -> dict:
    return create_client_process(client)


def edit_client_handler(client, number_id) -> dict:
    return edit_client_process(client, number_id)


def delete_client_handler(delete_id) -> dict:
    return delete_client_process(delete_id)


def show_client_handler() -> dict:
    return show_client_process()


def upload_file_handler(
        preventive_review,
        corrective_sheet,
        date_id_register
            ) -> dict:
    return upload_file_process(
        preventive_review,
        corrective_sheet,
        date_id_register)
