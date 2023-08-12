from abc import ABC, abstractmethod
from pathlib import Path

from settings import USER
from src.user.user import User


class UI(ABC):
    def __init__(self):
        self.user = None

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def get_user(self) -> dict:
        pass

