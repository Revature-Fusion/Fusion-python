from repositories.user_repo import UserRepo


class UserService:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def login(self, user):
        return self.user_repo.login(user)

    def create_guest(self, guest):
        return self.user_repo.create_guest(guest)

    def create_user(self, user):
        return self.user_repo.create_user(user)

    def get_user(self, u_id):
        return self.user_repo.get_user(u_id)

    def get_all_users(self):
        return self.user_repo.get_all_users()

    def update_user(self, change):
        return self.user_repo.update_user(change)

    def delete_user(self, u_id):
        return self.user_repo.delete_user(u_id)
