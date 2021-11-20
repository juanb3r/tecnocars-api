import hashlib


def hash_md5_utils(password: str) -> str:
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
