import math
import requests
from datetime import datetime

from settings import SJ_RESPONSE, SJ_KEY
from src.api.api import API


class SuperJobAPI(API):
    def __init__(self):
        super().__init__()
        self.response_file = SJ_RESPONSE

    def get_vacancies(self, search_query: str, page=None, per_page=100,
                      page_limit=None, source=False) -> dict:
        """
        Возвращает список вакансий по запросу

        :param search_query: Поисковой запрос
        :param page: Страница ответа
        :param per_page: Количество вакансий на странице (не более 100)
        :param page_limit: Максимальное количество страниц (не более 500)
        :param source: True - если необходимо вернуть полученные данные в исходном виде
        :return:
        """

        url = 'https://api.superjob.ru/2.0/vacancies/'
        headers = {'X-Api-App-Id': SJ_KEY}
        params = {'keyword': search_query,
                  'count': per_page,
                  'page': page
                  }
        print('Запрос вакансий SuperJob')
        response = requests.get(url, headers=headers, params=params).json()

        # Определение максимального количества страниц
        if math.ceil(response.get('total') / per_page) < 600 // per_page:
            pages = math.ceil(response.get('total') / per_page)
        else:
            pages = 600 // per_page
        if page_limit is None or page_limit > pages:
            page_limit = pages

        # Перебор страниц и получение данных
        vacancies = list()
        if response.get('total'):
            if page is None:
                params["page"] = 0
                while params["page"] != page_limit:
                    print(f'\rПолучение данных (станица {params["page"] + 1} из {page_limit})', end='')
                    response = requests.get(url, headers=headers, params=params).json()
                    vacancies.extend(response.get("objects"))
                    params["page"] += 1
                print('\rSuperJob - Ok')
            else:
                vacancies = response.get("objects")
                print('SuperJob - Ok')
        else:
            print('SuperJob - Отсутствуют вакансии по запросу')
        if source:
            return vacancies
        return self.normalization_data(vacancies)

    @staticmethod
    def normalization_data(vacancies: list[dict], **kwargs) -> dict:
        """
        Приведение полученных данных о вакансиях
        в формате SuperJob к формату приложения

        :param vacancies: исходные данные о вакансиях HeadHunter
        :return:
        """
        normal = dict()
        for item in vacancies:
            vacancy_id: str = f'SJ_{item.get("id")}'
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

            normal[vacancy_id] = {'service': 'SuperJob',
                                  'title': name,
                                  'date': date,
                                  'area': area,
                                  'currency': currency,
                                  'salary_fom': salary_from,
                                  'salary_to': salary_to,
                                  'url': url
                                  }
        return normal
