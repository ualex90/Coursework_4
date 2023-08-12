import pytest

from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI
from src.ui.ui import UI
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
    return Vacancy('HH_1111',
                   'HeadHunter',
                   'Тест vacancy_1',
                   '01.09.2023',
                   'World',
                   'RUR',
                   1000,
                   1000,
                   'https://dev.hh.ru/'
                   )


@pytest.fixture
def vacancy_2():
    return Vacancy('SJ_1111',
                   'SuperJob',
                   'Тест vacancy_2',
                   '01.09.2023',
                   'World',
                   'RUR',
                   0,
                   0,
                   'https://api.superjob.ru/',
                   True
                   )


@pytest.fixture
def vacancies_dict_1():
    return {'HH_0001': {'service': 'HeadHunter',
                        'title': 'Тест vacancy_1',
                        'date': '01.09.2023',
                        'area': 'World',
                        'currency': 'RUR',
                        'salary_fom': 1000,
                        'salary_to': 1000,
                        'url': 'https://dev.hh.ru/',
                        'is_favorite': False,
                        'is_to_removed': False
                        }}


@pytest.fixture
def vacancies_dict_2():
    return {'HH_0002': {'service': 'HeadHunter',
                        'title': 'Тест vacancy_2',
                        'date': '01.09.2023',
                        'area': 'World',
                        'currency': 'RUR',
                        'salary_fom': 1000,
                        'salary_to': 1000,
                        'url': 'https://dev.hh.ru/',
                        'is_favorite': False,
                        'is_to_removed': False
                        },
            'SJ_0001': {'service': 'SuperJob',
                        'vacancy_id': 'SJ_0001',
                        'title': 'Тест vacancy_3',
                        'date': '01.09.2023',
                        'area': 'World',
                        'currency': 'RUR',
                        'salary_fom': 1000,
                        'salary_to': 1000,
                        'url': 'https://api.superjob.ru/',
                        'is_favorite': False,
                        'is_to_removed': False
                        }}


@pytest.fixture
def vacancies_dict_3():
    return {'HH_0003': {'service': 'HeadHunter',
                        'title': 'Тест vacancy_4',
                        'date': '01.09.2023',
                        'area': 'World',
                        'currency': 'RUR',
                        'salary_fom': 1000,
                        'salary_to': 1000,
                        'url': 'https://dev.hh.ru/',
                        'is_favorite': True,
                        'is_to_removed': False
                        },
            'SJ_0002': {'service': 'SuperJob',
                        'title': 'Тест vacancy_5',
                        'date': '01.09.2023',
                        'area': 'World',
                        'currency': 'RUR',
                        'salary_fom': 1000,
                        'salary_to': 1000,
                        'url': 'https://api.superjob.ru/',
                        'is_favorite': False,
                        'is_to_removed': False
                        },
            'SJ_0003': {'service': 'SuperJob',
                        'title': 'Тест vacancy_6',
                        'date': '01.09.2023',
                        'area': 'World',
                        'currency': 'RUR',
                        'salary_fom': 1000,
                        'salary_to': 1000,
                        'url': 'https://api.superjob.ru/',
                        'is_favorite': False,
                        'is_to_removed': True
                        }}


@pytest.fixture
def text_ui_1():
    user = {'user_name': 'AnyKey'}
    return UI(user)


@pytest.fixture
def text_ui_2():
    user = dict()
    return UI(user)
