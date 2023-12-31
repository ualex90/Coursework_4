from settings import USER_FILE
from src.config.config import Config
from src.utils.file_manager import YAMLManager


class User(Config):
    """Класс пользователь"""
    config = YAMLManager(USER_FILE)

    def __init__(self, **kwargs):
        """
        Инициализация пользовательских параметров
        :param service: сервис для поиска (0: HH + SJ, 1: HH, 2: SJ)
        :param kwargs:
        """
        super().__init__()
        self.name = kwargs.get('name')
        self._service = kwargs.get('_service') if kwargs.get('_service') else 1
        self._sort = kwargs.get('_sort') if kwargs.get('_sort') else {'attribute': 'favorite', 'reverse': True}
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
