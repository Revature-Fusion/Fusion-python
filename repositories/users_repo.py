from abc import ABC, abstractmethod


class UsersRepo(ABC):

    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def get_user(self, u_id):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def update_user(self, change):
        pass

    @abstractmethod
    def delete_user(self, u_id):
        pass

