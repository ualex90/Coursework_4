from abc import ABC, abstractmethod
import json
from json import JSONDecodeError
from pathlib import Path

import yaml

from settings import FIXTURES
from src.vacancies.vacancies import Vacancies


class FileManager(ABC):
    """Абстрактный класс для работы с файлами"""
    def __init__(self, file_name) -> None:
        """
        Инициализация
        :param file_name: Имя файла
        """
        self.file = Path(FIXTURES, file_name)

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self, data, mode):
        pass


class JSONManager(FileManager):

    @staticmethod
    def make_dict(vacancies: Vacancies) -> dict:
        """Формирование словаря из объекта Vacancy"""

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
        :return: словарь с данными из файла
        """
        try:
            with open(self.file, 'r', encoding='UTF-8') as json_file:
                data = json.load(json_file)
        except JSONDecodeError:
            return dict()
        except FileNotFoundError:
            print(f'Файл не найден {self.file}')
            return dict()
        return data

    def save(self, data, mode='w'):
        """
        Сохранение данных в файл. Если файла не существует, он будет создан.
        :param data: исходные данные
        :param mode: режим переписывания файла "w", дописывания "a"
        """
        if not Path(self.file).exists():
            mode = 'a'
        with open(self.file, mode, encoding='UTF-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def save_vacancies(self, vacancies: Vacancies):
        """
        Обновление файла с вакансиями из списка вакансий
        """
        if Path(self.file).exists():
            data = self.load()
            data.update(self.make_dict(vacancies))
            mode = 'w'
        else:
            data = self.make_dict(vacancies)
            mode = 'a'

        with open(self.file, mode, encoding='UTF-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)


class YAMLManager(FileManager):

    def load(self) -> dict:
        """
        Чтение файла
        :return: словарь с данными из файла
        """
        try:
            with open(self.file, "r", encoding="UTF-8") as yaml_file:
                data = yaml.safe_load(yaml_file)
        except FileNotFoundError:
            print(f'Файл не найден {self.file}')
            return dict()
        return data

    def save(self, data, mode='w') -> None:
        """
        Сохранение данных в файл. Если файла не существует, он будет создан.
        :param data: исходные данные
        :param mode: режим переписывания файла "w", дописывания "a"
        """
        if not Path(self.file).exists():
            mode = 'a'
        with open(self.file, mode, encoding="UTF-8") as yaml_file:
            yaml.safe_dump(data, yaml_file, sort_keys=False, allow_unicode=True)