import os
from abc import ABC, abstractmethod

from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI
from src.utils.file_manager import JSONManager, YAMLManager
from src.vacancies.vacancies import Vacancies


class UI(ABC):
    def __init__(self):
        self.hh = HeadHunterAPI()  # объект для работы с API HeadHunter
        self.sj = SuperJobAPI()  # объект для работы с API HeadHunter
        self.vacancies = Vacancies()  # объект для добавления вакансий в список
        self.json_manager = JSONManager('test.json')  # объект для сохранения и чтения данных JSON
        self.yaml_manager = YAMLManager('test.yaml')  # объект для сохранения и чтения данных YAML
        self.hh_source = YAMLManager('hh_source.yaml')  # объект для сохранения исходных данных HH в YAML
        self.sj_source = YAMLManager('sj_source.yaml')  # объект для сохранения исходных данн
        self.operating_system = os.name
        self.user = None

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def get_user(self) -> dict:
        pass

