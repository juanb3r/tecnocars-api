import hashlib


def hash_md5_utils(password):
    hashed_password = hashlib.md5(password.encode())
    password = hashed_password.hexdigest()
    return password
