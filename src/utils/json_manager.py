import json
from json import JSONDecodeError
from pathlib import Path

from src.utils.file_manager import FileManager
from src.vacancies.vacancies import Vacancies


class JSONManager(FileManager):

    @staticmethod
    def make_json(vacancies: Vacancies) -> dict:
        data = dict()
        for item in vacancies.list:
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

    def load(self) -> dict:
        """
        Чтение файла
        :return:
        """
        try:
            with open(self.file, 'r', encoding='UTF-8') as json_file:
                data = json.load(json_file)
        except JSONDecodeError:
            return dict()
        return data

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

