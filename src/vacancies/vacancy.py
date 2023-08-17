class Vacancy:

    __slots__ = ('vacancy_id', 'service', 'title', 'date', 'area', 'currency',
                 'salary_fom', 'salary_to', 'url', '__is_to_removed', '__is_favorite')

    def __init__(self, vacancy_id: str, service: str, title: str, date: str, area: str, currency: str,
                 salary_fom: int, salary_to: int, url: str, is_favorite: bool = False) -> None:
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
        self.__is_to_removed = False
        self.__is_favorite = is_favorite

    @property
    def is_favorite(self) -> bool:
        return self.__is_favorite

    @is_favorite.setter
    def is_favorite(self, flag: bool) -> None:
        """
        Флаг отметки ИЗБРАННОЕ. Исключена одновременная
        установка в True вместе с флагом is_to_removed
        :param flag: Значение True/False
        """
        if isinstance(flag, bool):
            self.__is_favorite = flag
            if flag:
                self.__is_to_removed = False

    @property
    def is_to_removed(self) -> bool:

        return self.__is_to_removed

    @is_to_removed.setter
    def is_to_removed(self, flag: bool) -> None:
        """
        Флаг отметки К УДАЛЕНИЮ. Исключена одновременная
        установка в True вместе с флагом __is_favorite
        :param flag: Значение True/False
        """
        if isinstance(flag, bool):
            self.__is_to_removed = flag
            if flag:
                self.__is_favorite = False

    def __str__(self) -> str:
        salary = f'от {str(self.salary_fom)} до {str(self.salary_to)} {self.currency}'
        return f'Размещено на "{self.service}" {self.date}\n'\
               f'Название: {self.title}\n'\
               f'Регион: {self.area}\n'\
               f'Зарплата: {salary if self.salary_to else "Не указана"}\n'\
               f'Ссылка: {self.url}\n\n'\
               f'{"ОТМЕЧЕНО К УДАЛЕНИЮ" if self.__is_to_removed else "В ИЗБРАННОМ" if self.__is_favorite else ""}'
