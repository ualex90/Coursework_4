from datetime import datetime

import requests

from settings import HH_RESPONSE
from src.api.api import API


class HeadHunterAPI(API):
    def __init__(self):
        super().__init__()
        self.response_file = HH_RESPONSE

    def get_vacancies(self, search_query: str, area=None, page=None,
                      per_page=50, page_limit=None, write_json=False) -> list[dict]:
        """
        Возвращает список вакансий по запросу.
        Можно за раз получить не более 2000 вакансий

        :param search_query: Поисковой запрос
        :param area: Регион
        :param page: Страница ответа
        :param per_page: Количество вакансий на странице (не более 50)
        :param write_json: True - если необходимо сохранить ответ сервиса в файл
        :param page_limit: Количество страниц (максимум 40 при per_page=50)
        :return:
        """
        # Инициализация запроса
        url = 'https://api.hh.ru/vacancies'
        params = {'text': search_query,
                  'area': area,
                  'page': page,
                  'per_page': per_page
                  }
        print('Запрос вакансий HeadHunter')
        response = requests.get(url, params=params).json()

        # Определение максимального количества страниц
        if page_limit is None or page_limit > response.get('pages'):
            pass
            page_limit = response.get('pages')

        # Перебор страниц и получение данных
        vacancies = response.get('items')
        if vacancies:
            if page is None:
                params["page"] = 0
                while response.get('page') != (page_limit - 1):
                    print(f'\rПолучение данных (станица {params["page"] + 1} из {page_limit})', end='')
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

        # Возврат нормализованного списка
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
            if item.get('salary'):
                if item.get('salary').get('currency'):
                    currency: str = item.get('salary').get('currency')
                else:
                    currency: str = 'None'
                if item.get('salary').get('from') and item.get('salary').get('to'):
                    salary_from: int = int(item.get('salary').get('from'))
                    salary_to: int = int(item.get('salary').get('to'))
                elif item.get('salary').get('from'):
                    salary_from: int = int(item.get('salary').get('from'))
                    salary_to: int = salary_from
                elif item.get('salary').get('to'):
                    salary_to: int = int(item.get('salary').get('to'))
                    salary_from: int = salary_to
                else:
                    salary_from: int = 0
                    salary_to: int = 0
            else:
                currency: str = 'None'
                salary_from: int = 0
                salary_to: int = 0
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
