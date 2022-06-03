from repositories.users_repo import UsersRepo


class UsersService:
    def __init__(self, users_repo: UsersRepo):
        self.users_repo = users_repo

    def create_user(self, user):
        pass

    def get_user(self, u_id):
        pass

    def get_all_users(self):
        pass

    def update_user(self, change):
        pass

    def delete_user(self, u_id):
        pass

