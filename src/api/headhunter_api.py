import requests

from settings import HH_VACANCIES
from src.api.api import API


class HeadHunterAPI(API):
    def __init__(self):
        super().__init__()
        self.file = HH_VACANCIES

    def get_vacancies(self, search_query, area=1, page=None, per_page=50):
        """
        Возвращает список вакансий по запросу
        :param search_query:
        :param area:
        :param page:
        :param per_page:
        :return:
        """
        url = 'https://api.hh.ru/vacancies'
        params = {'text': search_query,
                  'area': area,
                  'page': page,
                  'per_page': per_page
                  }
        response = requests.get(url, params=params).json()

        if page is None:
            params["page"] = 0
            while response.get('page') <= 40 and response.get('page') != (response.get('pages') - 1):
                print(f'\rПолучение данных (станица {params["page"] + 1} из {response.get("pages")})', end='')
                response = requests.get(url, params).json()
                self.response.extend(response.get('items'))
                params["page"] += 1
        else:
            self.response = response.get('items')
        return None
