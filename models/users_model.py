from enums.role import Role

class Users:

    def __init__(self, u_id=0, email="", first_name="", last_name="", role=Role):
        self.u_id = u_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def __repr__(self):
        return str({
            "u_id": self.u_id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role
        })

    def json(self):
        return {
            "uId": self.u_id,
            "email": self.email,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "role": self.role
        }
