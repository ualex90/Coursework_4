from abc import ABC, abstractmethod


class Area(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
