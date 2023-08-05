import json
import yaml
from abc import ABC, abstractmethod


class API(ABC):
    def __init__(self):
        self.response_file = None

    @abstractmethod
    def get_vacancies(self, search_query: str) -> list[dict]:
        pass

    @abstractmethod
    def normalization_data(self, data: list[dict]) -> list[dict]:
        pass

    def write_yaml(self, data) -> None:
        with open(self.response_file, "w", encoding="UTF-8") as yaml_file:
            yaml.safe_dump(data, yaml_file, sort_keys=False, allow_unicode=True)
