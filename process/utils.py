import hashlib
import os


def hash_md5_util(password: str) -> str:
    """
    Hashcheamos la contraseña con md5

    Args:
        password (str): clave plana

    Returns:
        str: clave en md5
    """
    hashed_password = hashlib.md5(password.encode())
    password = hashed_password.hexdigest()
    return password


def delete_client_util(client: object) -> bool:
    client_id = (client.id_register).replace("_", "/")
    if os.path.exists(client_id):
        os.remove(client_id + "/corrective_sheet.jpg")
        os.remove(client_id + "/preventive_review.jpg")
        os.rmdir(client_id)
        if os.path.exists(client_id):
            return False
        else:
            return True
    else:
        False


def create_path_util(
    preventive_review,
    corrective_sheet,
    date_id_register: str
) -> dict:
    file_1, file_2, file_3, file_4, file_5 = date_id_register.split("_")
    path_file = file_1
    try:
        if not os.path.exists(path_file):
            os.mkdir(path_file)
        path_file += "/" + file_2
        if not os.path.exists(path_file):
            os.mkdir(path_file)
        path_file += "/" + file_3
        if not os.path.exists(path_file):
            os.mkdir(path_file)
        path_file += "/" + file_4
        if not os.path.exists(path_file):
            os.mkdir(path_file)
        path_file += "/" + file_5
        if not os.path.exists(path_file):
            os.mkdir(path_file)

        name_file_1 = str(
            path_file +
            "/preventive_review.jpg")
        f = open(name_file_1, "wb")
        f.write(preventive_review)
        f.close()

        name_file_2 = str(
                path_file +
                "/corrective_sheet.jpg")
        f = open(name_file_2, "wb")
        f.write(corrective_sheet)
        f.close()
        return {"data": {"message": "Archivos subidos exitosamente"}}

    except Exception:
        return {"data": {"message": "Error al subir los archivos"}}


class SessionManager:
    def __init__(self) -> None:
        self.user = {}
        self.value = False
