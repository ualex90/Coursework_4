import pytest

from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI
from src.vacancies.vacancy import Vacancy


@pytest.fixture
def hh():
    return HeadHunterAPI()


@pytest.fixture
def sj():
    return SuperJobAPI()


@pytest.fixture
def vacancy_1():
    return Vacancy(**{'service': 'SuperJob',
                      'vacancy_id': 1111,
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
                      'vacancy_id': 1111,
                      'name': 'Тест vacancy_2',
                      'date': '01.09.2023',
                      'area': 'World',
                      'currency': 'RUR',
                      'salary_fom': 0,
                      'salary_to': 0,
                      'url': 'https://api.superjob.ru/'
                      })