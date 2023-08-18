from settings import CONFIG_FILE
from src.config.config import Config
from src.utils.file_manager import YAMLManager


class ConfigTool(Config):
    """Конфигуратор программы"""

    config = YAMLManager(CONFIG_FILE)

    def __init__(self, **kwargs):
        super().__init__()
        self._is_hh_source = kwargs.get('_is_hh_source') if kwargs.get('_is_hh_source') else False
        self._is_sj_source = kwargs.get('_is_sj_source') if kwargs.get('_is_sj_source') else False
        self._is_vacancies_log = kwargs.get('_is_vacancies_log') if kwargs.get('_is_vacancies_log') else True
        self._is_save_log = kwargs.get('_is_save_log') if kwargs.get('_is_save_log') else True
        self._hh_limit = kwargs.get('_hh_limit')
        self._sj_limit = kwargs.get('_sj_limit')

    @property
    def is_hh_source(self):
        return self._is_hh_source

    @is_hh_source.setter
    def is_hh_source(self, data: int):
        if isinstance(data, bool):
            self._is_hh_source = data
            self.save_config()

    @property
    def is_sj_source(self):
        return self._is_sj_source

    @is_sj_source.setter
    def is_sj_source(self, data: int):
        if isinstance(data, bool):
            self._is_sj_source = data
            self.save_config()

    @property
    def is_vacancies_log(self):
        return self._is_vacancies_log

    @is_vacancies_log.setter
    def is_vacancies_log(self, data: int):
        if isinstance(data, bool):
            self._is_vacancies_log = data
            self.save_config()

    @property
    def is_save_log(self):
        return self._is_save_log

    @is_save_log.setter
    def is_save_log(self, data: int):
        if isinstance(data, bool):
            self._is_save_log = data
            self.save_config()

    @property
    def hh_limit(self):
        return self._hh_limit

    @hh_limit.setter
    def hh_limit(self, data: int):
        if isinstance(data, int):
            if 0 < data <= 40:
                self._hh_limit = data
                self.save_config()
            elif data > 40:
                self._hh_limit = 40
                self.save_config()

    @property
    def sj_limit(self):
        return self._sj_limit

    @sj_limit.setter
    def sj_limit(self, data: int):
        if isinstance(data, int):
            if 0 < data <= 6:
                self._sj_limit = data
                self.save_config()
            elif data > 6:
                self._sj_limit = 6
                self.save_config()
