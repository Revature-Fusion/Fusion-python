from abc import ABC, abstractmethod


class LoginRepo(ABC):

    @abstractmethod
    def login(self, user):
        pass
