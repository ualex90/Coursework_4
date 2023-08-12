from abc import ABC, abstractmethod


class UI(ABC):
    def __init__(self):
        self.user = None

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def get_user(self) -> dict:
        pass

