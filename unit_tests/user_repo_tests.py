import unittest
from models.user_model import User
from repositories.user_repo_impl import UserRepoImpl

ur = UserRepoImpl()
user = User(email="test3", first_name="testfname", last_name="testlname", username="testusername",
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
        print(ur.get_user(1))

    def test_dget_all_user(self):
        print(ur.get_all_users())

    def test_eupdate_user(self):
        user = ur.get_user(4)
        user.name = "test14"
        user = ur.update_user(user)
        print(user)

    def test_fdelete_user(self):
        user = ur.get_user(4)
        ur.delete_user(user.u_id)
        print(ur.get_all_users())