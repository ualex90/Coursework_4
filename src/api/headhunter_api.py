from datetime import datetime

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
        print('Запрос вакансий HeadHunter')
        response = requests.get(url, params=params).json()
        vacancies = response.get('items')
        if vacancies:
            if page is None:
                params["page"] = 0
                while response.get('page') <= 40 and response.get('page') != (response.get('pages') - 1):
                    print(f'\rПолучение данных (станица {params["page"] + 1} из {response.get("pages")})', end='')
                    response = requests.get(url, params).json()
                    vacancies.extend(vacancies)
                    params["page"] += 1
                print('\rHeadHunter - Ok')
            else:
                print('HeadHunter - Ok')

            if write_json:
                self.write_yaml(vacancies)
        else:
            print('HeadHunter - Отсутствуют вакансии по запросу')

        return self.normalization_data(vacancies)

    @staticmethod
    def normalization_data(vacancies: list[dict], **kwargs) -> list[dict]:
        """
        Приведение полученных данных о вакансиях
        в формате HeadHunter к формату приложения

        :param vacancies: исходные данные о вакансиях HeadHunter
        :return:
        """
        normal = list()
        for item in vacancies:
            vacancy_id: int = int(item.get('id'))
            name: str = item.get('name')
            date: str = datetime.fromisoformat(item.get('published_at')).strftime("%d.%m.%Y")
            area: str = item.get('area').get('name').partition(',')[0] if item.get('area') else 'None'
            currency: str = item.get('salary').get('currency') if item.get('salary') else 'None'
            if item.get('salary'):
                if item.get('salary').get('from') and item.get('salary').get('to'):
                    salary_from: float = float(item.get('salary').get('from'))
                    salary_to: float = float(item.get('salary').get('to'))
                elif item.get('salary').get('from'):
                    salary_from: float = float(item.get('salary').get('from'))
                    salary_to: float = salary_from
                else:
                    salary_to: float = float(item.get('salary').get('to'))
                    salary_from: float = salary_to
            else:
                salary_from: float = 0
                salary_to: float = 0
            url: str = item.get('alternate_url')

            normal.append({'service': 'HeadHunter',
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
