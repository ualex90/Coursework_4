import requests
from datetime import datetime

from settings import SJ_RESPONSE, SJ_KEY
from src.api.api import API


class SuperJobAPI(API):
    def __init__(self):
        super().__init__()
        self.response_file = SJ_RESPONSE

    def get_vacancies(self, search_query, write_json=False):
        """
        Возвращает список вакансий по запросу
        :param write_json:
        :param search_query:
        :return:
        """
        url = 'https://api.superjob.ru/2.0/vacancies'
        headers = {'X-Api-App-Id': SJ_KEY}
        params = {'keyword': search_query}

        response = requests.get(url, headers=headers, params=params).json()
        vacancies = response.get("objects")

        if write_json:
            self.write_yaml(vacancies)

        return self.normalization_data(vacancies)

    def normalization_data(self, data: list[dict]) -> list[dict]:
        normal_data = list()
        for item in data:
            normal_data.append({'service': 'SuperJob',
                                'vacancy_id': item.get('id'),
                                'name': item.get('profession'),
                                'date': datetime.fromtimestamp(item.get('date_published')).strftime("%d.%m.%Y"),
                                'area': item.get('address').partition(',')[0] if item.get('address') else 'None',
                                })
        return normal_data
