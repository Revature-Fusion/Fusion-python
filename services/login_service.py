from repositories.login_repo import LoginRepo


class LoginService:

    def __init__(self, login_repo: LoginRepo):
        self.login_repo = login_repo

    def login(self, user):
        return self.login_repo.login(user)


