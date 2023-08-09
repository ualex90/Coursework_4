class Vacancy:

    def __init__(self, data: dict):
        """
        Инициализация
        """
        key = tuple(data.keys())[0]
        value = tuple(data.values())[0]

        self.vacancy_id = key
        self.service = value.get('service')
        self.title = value.get('title')
        self.date = value.get('date')
        self.area = value.get('area')
        self.currency = value.get('currency')
        self.salary_fom = value.get('salary_fom')
        self.salary_to = value.get('salary_to')
        self.url = value.get('url')

    def __str__(self):
        return f'''Название: "{self.title}"
Регион: {self.area}
Зарплата: {str(self.salary_to) + " " + self.currency if self.salary_to else 'Не указана'}
Ссылка: {self.url}
'''
