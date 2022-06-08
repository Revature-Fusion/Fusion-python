import unittest
from models.user_model import User
from repositories.user_repo_impl import UserRepoImpl

ur = UserRepoImpl()
user = User(email="test1", first_name="testfname", last_name="testlname", username="testusername",
            password="testpassword", role="MEMBER")
guest = User(email="guestemail", first_name="guestfname", last_name="guestlname")


class TestUsersRep(unittest.TestCase):

    def test_acreate_user(self):
        user1 = ur.create_user(user)
        print(user1)

    def test_bcreate_guest(self):
        guest1 = ur.create_guest(guest)
        print(guest1)

    def test_cget_user(self):
        pass

    def test_dget_all_user(self):
        pass

    def test_eupdate_user(self):
        pass

    def test_fdelete_user(self):
        pass

