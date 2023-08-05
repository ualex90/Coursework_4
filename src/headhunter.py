import requests

from src.area import Area


class HeadHunter(Area):

    def get_vacancies(self, **kwargs):
        """
        Возвращает JSON на запрос по вакансиям
        :param kwargs:
        :return:
        """

        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': kwargs.get('text'),
            'area': kwargs.get('area'),
            'page': kwargs.get('page'),
            'per_page': kwargs.get('per_page')
        }
        request = requests.get('https://api.hh.ru/vacancies', params).json()
        return request

    # def write_json(self):
    #     with open() as file:


if __name__ == '__main__':
    hh = HeadHunter()
    search_query = {
        'text': 'инженер по КИПиА',
        'area': 1,
        'page': 0,
        'per_page': 100
    }
    print(hh.get_vacancies(**search_query))
