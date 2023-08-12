from pathlib import Path

from settings import USER
from src.utils.file_manager import YAMLManager


class User:
    """Класс пользователь"""
    config = YAMLManager(USER)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.save_config()

    @classmethod
    def init_yaml(cls):
        return cls(**cls.config.load())

    def save_config(self):
        self.config.save(self.__dict__)