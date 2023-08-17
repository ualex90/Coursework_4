from src.utils.file_manager import YAMLManager


class Config:

    config = YAMLManager('FILE')

    def __init__(self, **kwargs):
        pass

    @classmethod
    def init_yaml(cls):
        """Инициализация экземпляра класса из файла"""
        return cls(**cls.config.load())

    def save_config(self):
        """Сохранение полей инициализации в файл"""
        self.config.save(self.__dict__)
