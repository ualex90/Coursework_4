import json
from json import JSONDecodeError
from pathlib import Path

from settings import FIXTURES
from src.vacancies.vacancies import Vacancies


class JSONSaver:
    def __init__(self, file_name):
        self.file = Path(FIXTURES, file_name)

    @staticmethod
    def make_json(vacancies: Vacancies) -> dict:
        data = dict()
        for item in vacancies.data:
            data[item.vacancy_id] = {'service': item.service,
                                     'title': item.title,
                                     'date': item.date,
                                     'area': item.area,
                                     'currency': item.currency,
                                     'salary_fom': item.salary_fom,
                                     'salary_to': item.salary_to,
                                     'url': item.url
                                     }
        return data

    @staticmethod
    def normalization_data(data) -> dict:
        pass

    def load(self, update=True) -> dict:
        """
        Чтение файла
        :return:
        """
        try:
            with open(self.file, 'r', encoding='UTF-8') as json_file:
                data = json.load(json_file)
        except JSONDecodeError:
            return dict()
        if update:
            return data
        return self.normalization_data(data)

    def save(self, vacancies: Vacancies):
        """
        Обновление файла
        """
        if Path(self.file).exists():
            data = self.load()
            data.update(self.make_json(vacancies))
            mode = 'w'
        else:
            data = self.make_json(vacancies)
            mode = 'a'

        with open(self.file, mode, encoding='UTF-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

