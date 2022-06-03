from exceptions.login_exception import LoginException
from models.login_model import Login
from repositories.login_repo import LoginRepo
from util.db_connection import connection


def _login_user(record):
    return Login(u_id=record[0], username=record[1], password=record[2])


class LoginRepoImpl(LoginRepo):

    def login(self, user):
        sql = "SELECT * FROM users WHERE username = %s and password = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [user.username, user.password])
        connection.commit()

        record = cursor.fetchone()
        if record:
            return Login(record[0], record[1], record[2]).json()
        else:
            raise LoginException("Incorrect username or password")


