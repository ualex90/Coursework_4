from src.vacancies.vacancy import Vacancy


class Vacancies:
    def __init__(self):
        self.vacancies = list()

    def add_vacancies(self, data: list[dict], log=False) -> None:
        count = 0
        for item in data:
            self.vacancies.append(Vacancy(**item))
            count += 1
        self.print_log(count) if log else None

    def print_log(self, count) -> None:
        print('------------------------------------------')
        print(f'Добавлено вакансий: {count}')
        print(f'Вакансий в базе: {len(self.vacancies)}')
        print('------------------------------------------')
