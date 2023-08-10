class Vacancy:

    __slots__ = ('vacancy_id', 'service', 'title', 'date', 'area', 'currency', 'salary_fom', 'salary_to', 'url')

    def __init__(self, vacancy_id: str, service: str, title: str, date: str, area: str,
                 currency: str, salary_fom: int, salary_to: int, url: str) -> None:
        """
        Инициализация
        """
        self.vacancy_id = vacancy_id
        self.service = service
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
