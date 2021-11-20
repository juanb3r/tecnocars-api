from config.db_connection import session
from process.models import Users


class UserQuery():

    def __init__(self):
        self.session = session

    def show_users_tb(self) -> dict:
        try:
            users = self.session.query(Users).all()
            return {"data": {"users": users}}
        except Exception as error:
            return {"data": {"error": error}}

    def get_user_login_tb(self, username: str, password: str) -> dict:
        """
        Login del usuario

        Args:
            username (str): correo
            password (str): clave del usurio

        Returns:
            dict: Respuesta
        """
        try:
            user = self.session.query(Users).filter_by(
                username=username,
                password=password).one()
        except Exception:
            self.session.rollback()
            return {"data": {"message": "Verifique los datos"}}
        finally:
            self.session.close()
        return {"data": {"user": user}}

    def new_user_tb(self, user: object) -> dict:
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

    def edit_user_tb(self, user: object) -> dict:
        self.session.add(user)
        self.session.commit()
        self.session.close()
        return {"data": {"message": "El usuario fue editado"}}

    def delete_user_tb(self, id) -> dict:
        user = self.get_user_by_id_tb(id)
        self.session.delete(user)
        self.session.commit()
        self.session.close()
        return {"data": {"message": "El usuario fue borrado"}}
