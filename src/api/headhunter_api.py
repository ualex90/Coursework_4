import requests

from settings import HH_VACANCIES
from src.api.api import API


class HeadHunterAPI(API):
    def __init__(self):
        super().__init__()
        self.file = HH_VACANCIES

    def get_vacancies(self, text, area=1, page=None, per_page=50):
        """
        Возвращает JSON на запрос по вакансиям
        :param per_page:
        :param page:
        :param area:
        :param text:
        :return:
        """
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': text,
            'area': area,
            'page': page,
            'per_page': per_page
        }
        response = requests.get('https://api.hh.ru/vacancies', params).json()

        if page is None:
            params["page"] = 0
            while response.get('page') <= 40 and response.get('page') != (response.get('pages') - 1):
                print(f'\rПолучение данных (станица {params["page"] + 1} из {response.get("pages")})', end='')
                response = requests.get('https://api.hh.ru/vacancies', params).json()
                self.response.extend(response.get('items'))
                params["page"] += 1
        else:
            self.response = response.get('items')
        return None


