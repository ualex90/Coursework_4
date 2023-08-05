import requests

from settings import HH_RESPONSE
from src.api.api import API


class HeadHunterAPI(API):
    def __init__(self):
        super().__init__()
        self.response_file = HH_RESPONSE

    def get_vacancies(self, search_query: str, area=1, page=None, per_page=50, write_json=False) -> list[dict]:
        """
        Возвращает список вакансий по запросу
        :param search_query: Поисковой запрос
        :param area: Регион
        :param page: Страница ответа
        :param per_page: Количество вакансий на странице (не более 50)
        :param write_json: True - если необходимо сохранить ответ сервиса в файл
        :return:
        """
        vacancies = list()
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
                vacancies.extend(response.get('items'))
                params["page"] += 1
        else:
            vacancies = response.get('items')

        if write_json:
            self.write_yaml(vacancies)

        return self.normalization_data(vacancies)

    def normalization_data(self, data: list[dict]) -> list[dict]:
        return data
