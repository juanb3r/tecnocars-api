from config.db_connection import session
from process.models import Users


class UserQuery():

    def __init__(self) -> None:
        self.session = session

    def show_users_tb(self):
        try:
            users = self.session.query(Users).all()
            return users
        except Exception:
            return {"data": "error"}

    def get_user_login_tb(self, username: str, password: str):
        try:
            user = self.session.query(Users).filter_by(
                username=username,
                password=password).one()
        except Exception:
            self.session.rollback()
            return {"data": "Verifique los datos"}
        finally:
            self.session.close()
        return user

    def new_user_tb(self, user):
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
                return {"data": "El usuario fue creado"}
            elif(query_user >= 1):
                self.session.close()
                return {"data": "El usuario ya existe"}
            else:
                self.session.close()
                return {"data": "Correo erroneo"}

        except Exception:
            self.session.rollback()
            self.session.close()
            return {"data": "Error"}

    def edit_user_tb(self, user):
        self.session.add(user)
        self.session.commit()
        self.session.close()
        return True

    def delete_user_tb(self, id):
        user = self.get_user_by_id_tb(id)
        self.session.delete(user)
        self.session.commit()
        self.session.close()
        return True
