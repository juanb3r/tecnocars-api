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
        session_login: dict = {"user": user, "value": True}
        return session_login


class UserQuery():

    def __init__(self):
        self.session = session

    def show_users(self) -> dict:
        try:
            users = self.session.query(Users).all()
            return {"data": {"users": users}}
        except Exception as error:
            return {"data": {"error": error}}

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
            return {"data": {"message": "Verifique los datos"}}
        finally:
            self.session.close()
        return {"data": session_login}

    def new_user(self, user: object) -> dict:
        """
        Creacion del usuario

        Args:
            user (object): Datos del usuario, nombre, correo, contraseña

        Returns:
            dict: Respuesta
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
                return {"data": {"message": "El usuario fue creado"}}
            elif(query_user >= 1):
                self.session.close()
                return {"data": {"message": "El usuario ya existe"}}
            else:
                self.session.close()
                return {"data": {"message": "Correo erroneo"}}

        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {"data": {"Error": error}}

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
            return {"data": {"message": "El usuario fue editado"}}
        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {"data": {"erorr": f"{error}"}}

    def delete_user(self, number_id) -> dict:
        try:
            delete_user: Users = self.session.query(Users).filter_by(
                id=number_id).one()
            self.session.delete(delete_user)
            self.session.commit()
            self.session.close()
            return {"data": {"message": "El usuario fue borrado"}}
        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {"data": {"erorr": f"{error}"}}



class ClientQuery():

    def __init__(self):
        self.session = session

    def show_clients(self) -> dict:
        try:
            clients = self.session.query(Client).all()
            return {"data": {"clients": clients}}
        except Exception as error:
            return {"data": {"erorr": f"{error}"}}

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
            return {"data": {
                    "message": "El cliente fue creado",
                    "id_register": identify_unique
                    }}

        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {"data": {"erorr": f"{error}"}}

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
            return {"data": {"message": "Archivos subidos correctamente"}}

        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {"data": {"erorr": f"{error}"}}

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
            return {"data": {"message": "El usuario fue editado"}}

        except Exception as error:
            self.session.rollback()
            self.session.close()
            return {"data": {"erorr": f"{error}"}}

    def delete_client(self, delete_id) -> dict:
        client: Client = self.session.query(Client).filter_by(
                id=delete_id).one()
        response_delete_file = delete_client_util(client)
        if response_delete_file:
            self.session.delete(client)
            self.session.commit()
            self.session.close()
            return {"data": {"message": "El usuario fue borrado"}}
        else:
            return {"data": {"message": "El usuario no fue borrado"}}
