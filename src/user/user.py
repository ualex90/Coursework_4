from settings import USER
from src.utils.file_manager import YAMLManager


class User:
    """Класс пользователь"""
    config = YAMLManager(USER)

    def __init__(self, **kwargs):
        """
        Инициализация пользовательских параметров
        :param service: сервис для поиска (0: HH + SJ, 1: HH, 2: SJ)
        :param kwargs:
        """
        self.name = kwargs.get('name')
        self._service = kwargs.get('_service') if kwargs.get('_service') else 1
        self._sort = kwargs.get('_sort') if kwargs.get('_sort') else {'attribute': 'date', 'reverse': False}
        self.save_config()

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, data: int):
        if data in [1, 2, 3]:
            self._service = data
            self.save_config()

    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, data: dict):
        self._sort = data
        self.save_config()

    @classmethod
    def init_yaml(cls):
        """Инициализация экземпляра класса из файла"""
        return cls(**cls.config.load())

    def save_config(self):
        """Сохранение полей инициализации в файл"""
        self.config.save(self.__dict__)
