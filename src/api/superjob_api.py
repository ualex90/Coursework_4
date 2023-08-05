from settings import SJ_VACANCIES
from src.api.api import API


class SuperJobAPI(API):
    def __init__(self):
        super().__init__()
        self.file = SJ_VACANCIES

    def get_vacancies(self, text):
        pass
