from datetime import datetime
from config.db_connection import session
from process.models import Users, Client
from process.utils import delete_client_util


class Session():

    def __init__(self):
        self.session = session

    def login_session(self, username: str, password: str) -> dict:
        user = self.session.query(Users).filter_by(
                    username=username,
                    password=password).one()
        session_login: dict = {
            "user": {
                "id": user.id,
                "name": user.name,
                "username": user.username,
                "access": user.access
            },
            "value": True}
        return session_login


class UserQuery():

    def __init__(self):
        self.session = session

    def show_users(self) -> dict:
        users_show = []
        try:
            users = self.session.query(Users).all()
            for user in users:
                users_show.append({
                        "id": user.id,
                        "name": user.name,
                        "username": user.username,
                        "access": user.access
                        }
                    )
            return {
                "data": users_show,
                "message": "Consultas de los usuarios existentes.",
                "status": 200
            }
        except Exception as error:
            return {
                "data": {"error": f"{error}"},
                "message": "Hubo un error en la consulta de la base de datos",
                "status": 500
            }

    def get_user_login(self, username: str, password: str) -> dict:
        """
        Login del usuario

        Args:
            username (str): correo
            password (str): clave del usurio

        Returns:
            dict: Respuesta
        """
        try:
            session_login = Session().login_session(username, password)
        except Exception:
            self.session.rollback()
            return {
                "data": {"error": True},
                "message": "Verifique los datos, los datos son erróneos",
                "status": 204
            }
        finally:
            self.session.close()
        return {
            "data": session_login,
            "message": "Verifique los datos",
            "status": 200
        }

    def new_user(self, user: object) -> dict:
        """
        Creacion del usuario

        Args:
            user (object): Datos del usuario, nombre, correo, contraseña

        Returns:
            dict: {"data": {"message": }}
            1. El usuario fue creado
            2. El usuario ya existe
            3. Correo erroneo
            4. Error
        """
        try:
            query_user = self.session.query(Users).filter_by(
                username=user.username).count()
            if (query_user != 1 and len(user.username) > 5 and
                    (user.username).count("@") == 1):
                new_user = Users(
                    name=user.name,
                    username=user.username,
                    password=user.password,
                    access=user.access)
                self.session.add(new_user)
                self.session.commit()
                self.session.close()
                return {
                    "data": {},
                    "message": "El usuario fue creado",
                    "status": 200
                }
            elif(query_user >= 1):
                self.session.close()
                return {
                    "data": {},
                    "message": "El usuario ya existe",
                    "status": 409
                }
            else:
                self.session.close()
                return {
                    "data": {},
                    "message": "Correo erroneo",
                    "status": 400
                }

        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {
                "data": {"error": f"{error}"},
                "message": "Hubo un error con la base de datos",
                "status": 500
            }

    def edit_user(self, user: object, number_id) -> dict:
        try:
            edit_user: Users = self.session.query(Users).filter_by(
                id=number_id).one()
            edit_user.name = user.name
            edit_user.password = user.password
            edit_user.access = user.access
            edit_user.username = user.username

            self.session.add(edit_user)
            self.session.commit()
            self.session.close()
            return {
                "data": {
                    "id": number_id,
                    "name": user.name,
                    "username": user.username,
                    "access": user.access
                },
                "message": "El usuario fue editado",
                "status": 200
            }
        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {
                "data": {"erorr": f"{error}"},
                "message": "Hubo un error al consultar la base de datos",
                "status": 500
            }

    def delete_user(self, number_id) -> dict:
        try:
            delete_user: Users = self.session.query(Users).filter_by(
                id=number_id).one()
            self.session.delete(delete_user)
            self.session.commit()
            self.session.close()
            return {
                "data": {},
                "message": "El usuario fue borrado",
                "status": 200
            }
        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {
                "data": {"erorr": f"{error}"},
                "message": "Hubo un error",
                "status": 500
            }


class ClientQuery():

    def __init__(self):
        self.session = session

    def show_clients(self) -> dict:
        try:
            client_show = []
            clients = self.session.query(Client).all()
            for client in clients:
                client_show.append({
                    "id": client.id,
                    "id_register": client.id_register,
                    "placa_empresa": client.placa_empresa,
                    "placa": client.placa,
                    "aprobado": client.aprobado
                }
                )
            return {
                "data": client_show,
                "message": "Todos los clientes",
                "status": 200
            }
        except Exception as error:
            return {
                "data": {"erorr": f"{error}"},
                "message": "Hubo un error al consultar el cliente",
                "status": 500
            }

    def new_client(self, client: object) -> dict:
        time_now = datetime.now()
        time_path = f"{time_now.year}_{time_now.month}_{time_now.day}"
        try:
            identify_unique: str = str(client.empresa) + "_" +\
                str(client.placa) + "_" + str(time_path)

            client = dict(client)
            new_client = Client(**client)
            new_client.id_register = identify_unique
            self.session.add(new_client)
            self.session.commit()
            self.session.close()
            return {
                "data": {},
                "message": "El cliente fue creado",
                "id_register": identify_unique,
                "status": 200
            }

        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {
                "data": {"erorr": f"{error}"},
                "message": "Hubo un error en la consulta de la base de datos",
                "status": 500
            }

    def edit_client_path_file(
            self,
            date_id_register: str
    ) -> dict:
        try:
            client = self.session.query(Client).filter_by(
                id_register=date_id_register
            ).one()
            client.archivo = str(
                date_id_register.replace("_", "/") +
                "/preventive_review.jpg")
            client.archivo_2 = str(
                date_id_register.replace("_", "/") +
                "/corrective_sheet.jpg")

            self.session.add(client)
            self.session.commit()
            self.session.close()
            return {
                "data": {},
                "message": "Archivos subidos correctamente",
                "status": 200
            }

        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {
                "data": {"erorr": f"{error}"},
                "message": "Hubo un error al consultar la base de datos",
                "status": 500
            }

    def edit_client(self, client: object, number_id) -> dict:

        try:
            edit_client: Client = self.session.query(Client).filter_by(
                id=number_id).one()
            edit_client.empresa = client.empresa
            edit_client.placa_empresa = client.placa_empresa
            edit_client.placa = client.placa
            edit_client.bimensual = client.bimensual
            edit_client.soat = client.soat
            edit_client.tecnomecanica = client.tecnomecanica
            edit_client.poliza = client.poliza
            edit_client.fecha_registro = client.fecha_registro
            edit_client.aprobado = client.aprobado
            self.session.add(edit_client)
            self.session.commit()
            self.session.close()
            return {
                "data": client.placa,
                "message": "El usuario fue editado",
                "status": 200
            }

        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {
                "data": {"erorr": f"{error}"},
                "message": "Hubo un error en la consulta de los datos",
                "status": 500
            }

    def delete_client(self, delete_id) -> dict:
        try:
            client: Client = self.session.query(Client).filter_by(
                    id=delete_id).one()
            response_delete_file = delete_client_util(client)
            if response_delete_file:
                self.session.delete(client)
                self.session.commit()
                self.session.close()
                return {
                    "data": delete_id,
                    "message": "El usuario fue borrado",
                    "status": 200
                }
        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {
                "data": {"erorr": f"{error}"},
                "message": "El usuario no fue borrado",
                "status": 500
            }
