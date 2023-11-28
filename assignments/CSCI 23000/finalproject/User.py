from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def start(self):
        pass
