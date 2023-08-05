import json
from abc import ABC, abstractmethod


class AreaAPI(ABC):
    def __init__(self):
        self.response = list()
        self.file = None

    @abstractmethod
    def get_vacancies(self):
        pass

    def write_json(self):
        with open(self.file, 'w', encoding='UTF-8') as json_file:
            json.dump(self.response, json_file, ensure_ascii=False, indent=2)
