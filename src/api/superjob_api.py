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
        normal = list()
        for item in data:
            vacancy_id: int = int(item.get('id'))
            name: str = item.get('profession')
            date: str = datetime.fromtimestamp(item.get('date_published')).strftime("%d.%m.%Y")
            area: str = item.get('address').partition(',')[0] if item.get('address') else 'None'
            currency: str = 'RUR' if item.get('currency') == 'rub' else 'USD'
            salary_fom: float = float(item.get('payment_from')) if float(item.get('payment_from')) else None
            salary_to: float = float(item.get('payment_to')) if float(item.get('payment_to')) else salary_fom
            normal.append({'service': 'SuperJob',
                           'vacancy_id': vacancy_id,
                           'name': name,
                           'date': date,
                           'area': area,
                           'currency': currency,
                           'salary_fom': salary_fom,
                           'salary_to': salary_to
                           })
        return normal
