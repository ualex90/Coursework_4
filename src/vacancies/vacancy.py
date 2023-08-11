class Vacancy:

    __slots__ = ('vacancy_id', 'service', 'title', 'date', 'area', 'currency',
                 'salary_fom', 'salary_to', 'url', '__is_favorite', '__is_to_removed')

    def __init__(self, vacancy_id: str, service: str, title: str, date: str, area: str,
                 currency: str, salary_fom: int, salary_to: int, url: str, is_favorite: bool = False) -> None:
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
        self.__is_favorite = is_favorite
        self.__is_to_removed = False

    @property
    def is_favorite(self):
        return self.__is_favorite

    @is_favorite.setter
    def is_favorite(self, flag: bool):
        if isinstance(flag, bool):
            self.__is_favorite = flag

    @property
    def is_to_removed(self):
        return self.__is_to_removed

    @is_to_removed.setter
    def is_to_removed(self, flag: bool):
        if isinstance(flag, bool):
            self.__is_to_removed = flag

    def __str__(self):
        return f'''Название: "{self.title}"
Регион: {self.area}
Зарплата: {str(self.salary_to) + " " + self.currency if self.salary_to else 'Не указана'}
Ссылка: {self.url}
'''
