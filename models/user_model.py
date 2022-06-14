class User:

    def __init__(self, u_id=0, email="", first_name="", last_name="", username="", password="", role=""):
        self.u_id = u_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return str({
            "u_id": self.u_id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "password": self.password,
            "role": self.role
        })

    def json(self):
        return {
            "uId": self.u_id,
            "email": self.email,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }

    @staticmethod
    def json_parse(json):
        login = User()
        login.username = json['username']
        login.password = json['password']
        login.u_id = json['uId'] if 'uId' in json else 0
        return login


# class Login:
#
#     def __init__(self, u_id=0, username="", password="", first_name="", last_name=""):
#         self.u_id = u_id
#         self.username = username
#         self.password = password
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def json(self):
#         return {
#             "uId": self.u_id,
#             "username": self.username,
#             "password": self.password,
#             "firstName": self.first_name,
#             "lastName": self.last_name
#         }
#
#     @staticmethod
#     def json_parse(json):
#         login = Login()
#         login.username = json['username']
#         login.password = json['password']
#         login.u_id = json['uId'] if 'uId' in json else 0
#         return login
#
#     def __repr__(self):
#         return str(self.json())
#
#     def __eq__(self, other):
#         if not other:
#             return False
#
#         if not isinstance(other, Login):
#             return False
#
#         return self.__dict__ == other.__dict__
