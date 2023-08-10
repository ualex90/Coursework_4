from src.vacancies.vacancy import Vacancy


class Vacancies:
    def __init__(self):
        self.list = list()

    def add_vacancies(self, data: dict, log=False):
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
                                     value.get('url')
                                     ))
            count += 1
        if log:
            self.__print_log(count)
        return count

    def __print_log(self, count) -> None:
        """
        Вывод в консоль иформации о количестве
        вакансий добавленных в список вакансий
        :param count:
        :return:
        """
        print('------------------------------------------')
        print(f'Добавлено вакансий: {count}')
        print(f'Вакансий в базе: {len(self.list)}')
        print('------------------------------------------')
