import pytest

from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI
from src.vacancies.vacancies import Vacancies
from src.vacancies.vacancy import Vacancy


@pytest.fixture
def hh():
    return HeadHunterAPI()


@pytest.fixture
def sj():
    return SuperJobAPI()


@pytest.fixture
def vacancies():
    return Vacancies()


@pytest.fixture
def vacancy_1():
    return Vacancy(**{'service': 'HeadHunter',
                      'vacancy_id': 'HH_1111',
                      'name': 'Тест vacancy_1',
                      'date': '01.09.2023',
                      'area': 'World',
                      'currency': 'RUR',
                      'salary_fom': 1000,
                      'salary_to': 1000,
                      'url': 'https://dev.hh.ru/'
                      })


@pytest.fixture
def vacancy_2():
    return Vacancy(**{'service': 'SuperJob',
                      'vacancy_id': 'SJ_1111',
                      'name': 'Тест vacancy_2',
                      'date': '01.09.2023',
                      'area': 'World',
                      'currency': 'RUR',
                      'salary_fom': 0,
                      'salary_to': 0,
                      'url': 'https://api.superjob.ru/'
                      })


@pytest.fixture
def vacancies_list_1():
    return [{'service': 'HeadHunter',
             'vacancy_id': 'HH_0001',
             'name': 'Тест vacancy_1',
             'date': '01.09.2023',
             'area': 'World',
             'currency': 'RUR',
             'salary_fom': 1000,
             'salary_to': 1000,
             'url': 'https://dev.hh.ru/'
             }]


@pytest.fixture
def vacancies_list_2():
    return [{'service': 'HeadHunter',
             'vacancy_id': 'HH_0002',
             'name': 'Тест vacancy_2',
             'date': '01.09.2023',
             'area': 'World',
             'currency': 'RUR',
             'salary_fom': 1000,
             'salary_to': 1000,
             'url': 'https://dev.hh.ru/'
             },
            {'service': 'SuperJob',
             'vacancy_id': 'SJ_0001',
             'name': 'Тест vacancy_3',
             'date': '01.09.2023',
             'area': 'World',
             'currency': 'RUR',
             'salary_fom': 1000,
             'salary_to': 1000,
             'url': 'https://api.superjob.ru/'
             }]


@pytest.fixture
def vacancies_list_3():
    return [{'service': 'HeadHunter',
             'vacancy_id': 'HH_0003',
             'name': 'Тест vacancy_4',
             'date': '01.09.2023',
             'area': 'World',
             'currency': 'RUR',
             'salary_fom': 1000,
             'salary_to': 1000,
             'url': 'https://dev.hh.ru/'
             },
            {'service': 'SuperJob',
             'vacancy_id': 'SJ_0002',
             'name': 'Тест vacancy_5',
             'date': '01.09.2023',
             'area': 'World',
             'currency': 'RUR',
             'salary_fom': 1000,
             'salary_to': 1000,
             'url': 'https://api.superjob.ru/'
             },
            {'service': 'SuperJob',
             'vacancy_id': 'SJ_0003',
             'name': 'Тест vacancy_6',
             'date': '01.09.2023',
             'area': 'World',
             'currency': 'RUR',
             'salary_fom': 1000,
             'salary_to': 1000,
             'url': 'https://api.superjob.ru/'
             }]
