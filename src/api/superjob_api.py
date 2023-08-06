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

        :param search_query: Поисковой запрос
        :param write_json: True - если необходимо сохранить ответ сервиса в файл
        :return:
        """
        url = 'https://api.superjob.ru/2.0/vacancies'
        headers = {'X-Api-App-Id': SJ_KEY}
        params = {'keyword': search_query}

        print('Запрос вакансий SuperJob')
        response = requests.get(url, headers=headers, params=params).json()
        vacancies = response.get("objects")
        if vacancies:
            print('\rSuperJob - Ok')
            if write_json:
                self.write_yaml(vacancies)
        else:
            print('HeadHunter - Отсутствуют вакансии по запросу')
        return self.normalization_data(vacancies)

    @staticmethod
    def normalization_data(vacancies: list[dict], **kwargs) -> list[dict]:
        """
        Приведение полученных данных о вакансиях
        в формате SuperJob к формату приложения

        :param vacancies: исходные данные о вакансиях HeadHunter
        :return:
        """
        normal = list()
        for item in vacancies:
            vacancy_id: int = int(item.get('id'))
            name: str = item.get('profession')
            date: str = datetime.fromtimestamp(item.get('date_published')).strftime("%d.%m.%Y")
            area: str = item.get('address').partition(',')[0] if item.get('address') else 'None'
            if item.get('currency'):
                currency: str = 'RUR' if item.get('currency') == 'rub' else item.get('currency').upper()
            else:
                currency: str = 'None'
            if item.get('payment_from') and item.get('payment_to'):
                salary_from: int = item.get('payment_from')
                salary_to: int = item.get('payment_to')
            elif item.get('payment_from'):
                salary_from: int = item.get('payment_from')
                salary_to: int = salary_from
            elif item.get('payment_to'):
                salary_to: int = item.get('payment_to')
                salary_from: int = salary_to
            else:
                salary_to: int = 0
                salary_from: int = 0
            url: str = item.get('link')

            normal.append({'service': 'SuperJob',
                           'vacancy_id': vacancy_id,
                           'name': name,
                           'date': date,
                           'area': area,
                           'currency': currency,
                           'salary_fom': salary_from,
                           'salary_to': salary_to,
                           'url': url
                           })
        return normal
