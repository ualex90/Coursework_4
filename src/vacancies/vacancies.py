from src.vacancies.vacancy import Vacancy


class Vacancies:
    def __init__(self):
        self.data = list()

    def add_vacancies(self, data: dict, log=False) -> None:
        count = 0
        for key, value in data.items():
            self.data.append(Vacancy({key: value}))
            count += 1
        self.print_log(count) if log else None

    def print_log(self, count) -> None:
        print('------------------------------------------')
        print(f'Добавлено вакансий: {count}')
        print(f'Вакансий в базе: {len(self.data)}')
        print('------------------------------------------')
