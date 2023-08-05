import requests

from settings import SJ_VACANCIES, SJ_KEY
from src.api.api import API


class SuperJobAPI(API):
    def __init__(self):
        super().__init__()
        self.file = SJ_VACANCIES

    def get_vacancies(self, search_query):
        """
        Возвращает список вакансий по запросу
        :param search_query:
        :return:
        """
        url = 'https://api.superjob.ru/2.0/vacancies'
        headers = {'X-Api-App-Id': SJ_KEY}
        params = {'keyword': search_query}
        response = requests.get(url, headers=headers, params=params).json()
        self.response = response
        return None
