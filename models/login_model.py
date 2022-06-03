class Login:

    def __init__(self, u_id=0, username="", password=""):
        self.u_id = u_id
        self.username = username
        self.password = password

    def __repr__(self):
        return str({
            "u_id": self.u_id,
            "username": self.username,
            "password": self.password
        })

    def json(self):
        return {
            "uId": self.u_id,
            "username": self.username,
            "password": self.password
        }

    @staticmethod
    def json_parse(json):
        login = Login()
        login.username = json['username']
        login.password = json['password']
        login.u_id = json['uId'] if 'uId' in json else 0
        return login
