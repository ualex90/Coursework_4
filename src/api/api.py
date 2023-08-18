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
