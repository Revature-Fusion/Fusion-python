import unittest

# from models.login_model import Login
# from models.users_model import Users
# from repositories.users_repo_impl import UsersRepoImpl
#
# ur = UsersRepoImpl()
# user = Users(email="Test1", first_name="testname", last_name="testlast", role="testrole")
# login = Login(username="testuser", password="test123")

from models.user_model import User, Login
from repositories.user_repo_impl import UserRepoImpl

ur = UserRepoImpl()
user = User(email="test1", first_name="testfname", last_name="testlname", username="testusername",
            password="testpassword", role="MEMBER")
guest = User(email="guestemail", first_name="guestfname", last_name="guestlname")


class TestUsersRep(unittest.TestCase):

    def test_acreate_user(self):
        user1 = ur.create_user(user)
        print(user1)

    def test_create_guest(self):
        guest1 = ur.create_guest(guest)
        print(guest1)

    def test_bget_user(self):
        pass

    def test_cget_all_user(self):
        pass

    def test_dupdate_user(self):
        pass

    def test_edelete_user(self):
        pass

