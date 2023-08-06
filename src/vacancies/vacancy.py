class Vacancy:
    def __init__(self, service: str, vacancy_id: int, name: str,
                 date: str, area: str, currency: str,
                 salary_fom: float, salary_to: float, url: str):
        """
        Инициализация

        :param service: Сервис на котором размещена вакансия
        :param vacancy_id: id
        :param name: Название вакансии
        :param date: Дата размещения
        :param area: Регион
        :param currency: Валюта
        :param salary_fom: Зарплата от
        :param salary_to: Зарплата до
        :param url: Ссылка на вакансию
        """

        self.service = service
        self.vacancy_id = vacancy_id
        self.name = name
        self.date = date
        self.area = area
        self.currency = currency
        self.salary_fom = salary_fom
        self.salary_to = salary_to
        self.url = url
