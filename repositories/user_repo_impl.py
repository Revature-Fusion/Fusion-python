from exceptions.login_exception import LoginException
from exceptions.resource_not_found import ResourceNotFound
from models.user_model import User
from repositories.user_repo import UserRepo
from util.db_connection import connection
from models.user_model import Login


def _build_user(record):
    return User(u_id=record[0], email=record[1], first_name=record[2], last_name=record[3], username=record[4],
                password=record[5], role=record[6])


def _login_user(record):
    return Login(u_id=record[0], username=record[4], password=record[5])


class UserRepoImpl(UserRepo):

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

    def create_guest(self, guest):
        sql = "INSERT into users VALUES (DEFAULT,%s,%s,%s,NULL,NULL,'GUEST') RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [guest.email, guest.first_name, guest.last_name])

        connection.commit()
        record = cursor.fetchone()

        return _build_user(record)

    def create_user(self, user):
        sql = "INSERT into users VALUES (DEFAULT,%s,%s,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [user.email, user.first_name, user.last_name, user.username, user.password, user.role])

        connection.commit()
        record = cursor.fetchone()

        return _build_user(record)

    def get_user(self, u_id):

        sql = "SELECT * FROM users WHERE u_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [u_id])

        record = cursor.fetchone()

        if record:
            return _build_user(record)
        else:
            raise ResourceNotFound(f"User with id: {u_id} -Not Found")

    def get_all_users(self):
        sql = "SELECT * from users"

        cursor = connection.cursor()
        cursor.execute(sql)

        record = cursor.fetchall()

        return [_build_user(record) for record in record]

    def update_user(self, change):
        sql = "UPDATE users SET email=%s, first_name=%s, last_name=%s, username=%s, password=%s, role=%s WHERE u_id =%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.email, change.first_name, change.last_name, change.username, change.password,
                             change.role, change.u_id])

        connection.commit()
        record = cursor.fetchone()

        return _build_user(record)

    def delete_user(self, u_id):
        sql = "DELETE FROM users WHERE u_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [u_id])
        connection.commit()
