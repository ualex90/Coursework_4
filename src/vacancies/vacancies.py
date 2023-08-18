import os

from src.vacancies.vacancy import Vacancy


class Vacancies:
    def __init__(self):
        self.list = list()

    def add_vacancies(self, data: dict, log=False):
        """
        Добавление вакансий в список
        :param data: нормализованный словарь с вакансиями
        :param log: выводить/не выводить сообщение по количеству вакансий в консоль
        :return:
        """
        count = 0
        for key, value in data.items():
            self.list.append(Vacancy(key,
                                     value.get('service'),
                                     value.get('title'),
                                     value.get('date'),
                                     value.get('area'),
                                     value.get('currency'),
                                     value.get('salary_fom'),
                                     value.get('salary_to'),
                                     value.get('url'),
                                     value.get('is_favorite')
                                     ))
            count += 1
        if log:
            self.__print_log(count)
        return count

    def sorted(self, attribute: str = 'date', reverse: bool = False) -> None:
        """
        Сортировка списка вакансий по аттрибуту
        Можно задать только 1 аттрибут для сортировки

        :param attribute: Аттрибут объекта Vacancy
        :param reverse: сортировка по возврастанию/убыванию - True/False
        :return:
        """
        match attribute:
            case 'service':
                self.list.sort(key=lambda x: x.service, reverse=reverse)
            case 'title':
                self.list.sort(key=lambda x: x.title, reverse=reverse)
            case 'date':
                self.list.sort(key=lambda x: x.date, reverse=reverse)
            case 'area':
                self.list.sort(key=lambda x: x.area, reverse=reverse)
            case 'currency':
                self.list.sort(key=lambda x: x.currency, reverse=reverse)
            case 'salary':
                self.list.sort(key=lambda x: x.salary_to, reverse=reverse)
            case 'favorite':
                self.list.sort(key=lambda x: x.is_favorite, reverse=reverse)

    def search(self, search_query: str) -> list:
        """
        Поиск по названию вакансии
        :param search_query:
        :return:
        """
        result = list()
        for item in self.list:
            if search_query.lower() in item.title.lower().replace(',', ''):
                result.append(item)
        return result

    def __print_log(self, count) -> None:
        """
        Вывод в консоль иформации о количестве
        вакансий добавленных в список вакансий
        :param count:
        :return:
        """
        print(f'Добавлено вакансий: {count}')
        print(f'Вакансий в списке: {len(self.list)}')
        print('------------------------------------------')

    def __len__(self):
        return len(self.list)

    def __str__(self):
            [print(i) for i in self.list]
