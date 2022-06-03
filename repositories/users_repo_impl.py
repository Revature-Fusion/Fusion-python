from exceptions.resource_not_found import ResourceNotFound
from models.users_model import Users
from repositories.users_repo import UsersRepo
from util.db_connection import connection


def _build_user(record):
    return Users(u_id=record[0], email=record[1], first_name=record[2], last_name=record[3], role=record[4])


class UsersRepoImpl(UsersRepo):

    def create_user(self, user):
        sql = "INSERT into users VALUES (DEFAULT,%s,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [user.email, user.first_name, user.last_name, user.role])

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
        pass

    def update_user(self, change):
        pass

    def delete_user(self, u_id):
        pass
