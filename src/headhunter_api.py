import requests

from settings import HH_VACANCIES
from src.area_api import AreaAPI


class HeadHunterAPI(AreaAPI):
    def __init__(self):
        super().__init__()
        self.file = HH_VACANCIES

    def get_vacancies(self, **kwargs):
        """
        Возвращает JSON на запрос по вакансиям
        :param kwargs:
        :return:
        """
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': kwargs.get('text'),
            'area': kwargs.get('area') if kwargs.get('area') else 1,
            'page': kwargs.get('page'),
            'per_page': kwargs.get('per_page') if kwargs.get('per_page') else 50
        }
        response = requests.get('https://api.hh.ru/vacancies', params).json()

        if kwargs.get('page') is None:
            params["page"] = 0
            while response.get('page') <= 40 and response.get('page') != (response.get('pages') - 1):
                print(params.get("page"))
                response = requests.get('https://api.hh.ru/vacancies', params).json()
                self.response.extend(response.get('items'))
                params["page"] += 1
        else:
            self.response = response.get('items')
        return None


if __name__ == '__main__':
    hh = HeadHunterAPI()
    search_query = {
        'text': 'АСУТП',
        # 'page': 0,
        'per_page': 50
    }
    hh.get_vacancies(**search_query)
    hh.write_json()

