class Vacancy:
    __slots__ = ('service', 'vacancy_id', 'title',
                 'date', 'area', 'currency',
                 'salary_fom', 'salary_to', 'url')

    def __init__(self, service: str, vacancy_id: int, title: str,
                 date: str, area: str, currency: str,
                 salary_fom: int, salary_to: int, url: str):
        """
        Инициализация

        :param service: Сервис на котором размещена вакансия
        :param vacancy_id: id
        :param title: Название вакансии
        :param date: Дата размещения
        :param area: Регион
        :param currency: Валюта
        :param salary_fom: Зарплата от
        :param salary_to: Зарплата до
        :param url: Ссылка на вакансию
        """

        self.service = service
        self.vacancy_id = vacancy_id
        self.title = title
        self.date = date
        self.area = area
        self.currency = currency
        self.salary_fom = salary_fom
        self.salary_to = salary_to
        self.url = url

    def __str__(self):
        return f'''Название: "{self.title}"
Регион: {self.area}
Зарплата: {str(self.salary_to) + " " + self.currency if self.salary_to else 'Не указана'}
Ссылка: {self.url}
'''
