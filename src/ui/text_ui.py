import os
import time
from pathlib import Path

from settings import USER
from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI
from src.user.user import User
from src.utils.file_manager import JSONManager, YAMLManager
from src.vacancies.vacancies import Vacancies


class TextUI:
    """Пользовательский интерфейс"""

    def __init__(self):
        self.hh = HeadHunterAPI()  # объект для работы с API HeadHunter
        self.sj = SuperJobAPI()  # объект для работы с API HeadHunter
        self.vacancies = Vacancies()  # объект для добавления вакансий в список
        self.json_manager = JSONManager('test.json')  # объект для сохранения и чтения данных JSON
        self.yaml_manager = YAMLManager('test.yaml')  # объект для сохранения и чтения данных YAML
        self.hh_source = YAMLManager('hh_source.yaml')  # объект для сохранения исходных данных HH в YAML
        self.sj_source = YAMLManager('sj_source.yaml')  # объект для сохранения исходных данных SJ в YAML
        self.operating_system = os.name
        self.user = None
        self.sorted = dict()

    def main(self):
        """главный метод UI"""
        self.user = self.get_user()
        self.sorted = self.user.sort
        self.main_menu()

    def clear_screen(self):
        """
        Отправка команды на очистку экрана консоли
        в зависимости от операционной системы
        """
        if self.operating_system == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def get_user(self) -> User:
        """
        Инициализируем пользователя из файла, если файл есть и содержит имя пользователя
        в противном случае - создаем нового пользователя
        :return:
        """
        self.clear_screen()
        greetings = 'Добро пожаловать в JobParser'
        for i in greetings:
            print(i, end='')
            time.sleep(0.00)
        if Path(USER).exists():
            user = User.init_yaml()
            if user.name:
                print(f', ', end='')
                for i in user.name:
                    print(i, end='')
                    time.sleep(0.00)
                print(f'!')
                print('-' * (len(greetings) + len(user.name) + 3))
                return user
        print('!')
        user = User(name=input('Введите свое имя: '))
        print('-' * (len(greetings) + 1))
        self.get_user()
        return user

    def main_menu(self):
        """Основное меню"""
        print('<Что нужно сделать?>')
        print('1. Настроить параметры поиска\n'
              '2. Найти вакансии в сети, на выбранных площадках\n'
              '3. Найти вакансии в локальной базе данных\n'
              '4. Настроить программу\n'
              '5. Выход из программы'
              )
        match input('>> '):
            case '1':
                self.clear_screen()
                self.search_settings()
            case '2':
                self.clear_screen()
                self.search_in_service()
            case '3':
                self.clear_screen()
                self.search_in_base()
            case '4':
                pass
            case '5':
                self.clear_screen()
                print('Возвращайтесь! Работа сама себя не найдет))')
                return None
            case _:
                self.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести номер варианта ответа')
                self.main_menu()

    def search_settings(self):
        """Выбор сервиса поиска работы"""
        match self.user.service:
            case 1:
                label = [None, '>', ' ', ' ']
            case 2:
                label = [None, ' ', '>', ' ']
            case 3:
                label = [None, ' ', ' ', '>']
            case _:
                label = [None, ' ', ' ', ' ']

        print('<Выбор сервиса поска работы>')
        print(f'{label[1]} 1. SuperJob + HeadHunter\n'
              f'{label[2]} 2. HeadHunter\n'
              f'{label[3]} 3. SuperJob\n'
              f'  4. Назад, в главное меню'
              )
        match input('>> '):
            case '1':
                self.user.service = 1
                self.clear_screen()
                self.search_settings()
            case '2':
                self.user.service = 2
                self.clear_screen()
                self.search_settings()
            case '3':
                self.user.service = 3
                self.clear_screen()
                self.search_settings()
            case '4':
                self.clear_screen()
                self.main_menu()
            case _:
                self.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести номер варианта ответа')
                self.search_settings()

    def search_in_service(self):
        """Поиск вакансий в сети"""
        print('<Поиск работы на сервисах>')
        print('Для выхода в главное меню, введите "exit"\n'
              'Введите название вакансии:'
              )
        if (request := input('>> ').lower().strip()) == 'exit':
            self.clear_screen()
            self.main_menu()
        else:
            match self.user.service:
                case 1:
                    self.clear_screen()
                    self.vacancies.add_vacancies(self.hh.get_vacancies(request, page_limit=4), log=True)
                    self.vacancies.add_vacancies(self.sj.get_vacancies(request, page_limit=4), log=True)
                case 2:
                    self.clear_screen()
                    self.vacancies.add_vacancies(self.hh.get_vacancies(request, page_limit=4), log=True)
                case 3:
                    self.clear_screen()
                    self.vacancies.add_vacancies(self.sj.get_vacancies(request, page_limit=4), log=True)
            input('Для продолжения работы, нажмите ENTER')
            self.clear_screen()
            self.menu_service_vacancies()

    def menu_service_vacancies(self):
        print('<Выберете подходящий вариант>')
        print('1. Просмотр вакансий\n'
              '2. Новый поиск\n'
              '3. Сортировка\n'
              '4. Сохранить вакансии в локальную базу данных\n'
              '5. Главное меню'
              )
        match input('>> '):
            case '1':
                self.clear_screen()
                self.view_result('service')
            case '2':
                self.clear_screen()
                self.vacancies.list = []
                self.search_in_service()
            case '3':
                self.clear_screen()
                self.menu_sorted_result('service')
            case '4':
                self.clear_screen()
                self.json_manager.save_vacancies(self.vacancies, log=True)
                self.menu_service_vacancies()
            case '5':
                self.clear_screen()
                self.main_menu()
            case _:
                self.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести номер варианта ответа')
                self.menu_service_vacancies()

    def search_in_base(self):
        """Поиск вакансий в сети"""
        self.vacancies.add_vacancies(self.json_manager.load())
        print('<Поиск работы локальной базе данных>')
        print(f'Всего вакансий в базе {len(self.vacancies)}')
        print('Для выхода в главное меню, введите "exit"\n'
              'Введите название вакансии:'
              )
        if (request := input('>> ').lower().strip()) == 'exit':
            self.clear_screen()
            self.main_menu()
        else:
            self.vacancies.list = self.vacancies.search(request)
            self.clear_screen()
            print(f'Найдено вакансий: {len(self.vacancies)}')
            input('Для продолжения работы, нажмите ENTER')
            self.clear_screen()
            self.menu_base_vacancies()

    def menu_base_vacancies(self):
        print('<Выберете подходящий вариант>')
        print('1. Просмотр вакансий\n'
              '2. Новый поиск\n'
              '3. Сортировка\n'
              '4. Главное меню'
              )
        match input('>> '):
            case '1':
                self.clear_screen()
                self.view_result('base')
            case '2':
                self.clear_screen()
                self.vacancies.list = []
                self.search_in_base()
            case '3':
                self.clear_screen()
                self.menu_sorted_result('base')
            case '4':
                self.clear_screen()
                self.main_menu()
            case _:
                self.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести номер варианта ответа')
                self.menu_base_vacancies()

    def menu_sorted_result(self, source: str):

        match self.user.sort.get('attribute'):
            case 'service':
                label = [None, '>', ' ', ' ', ' ', ' ', ' ', ' ']
            case 'title':
                label = [None, ' ', '>', ' ', ' ', ' ', ' ', ' ']
            case 'date':
                label = [None, ' ', ' ', '>', ' ', ' ', ' ', ' ']
            case 'area':
                label = [None, ' ', ' ', ' ', '>', ' ', ' ', ' ']
            case 'currency':
                label = [None, ' ', ' ', ' ', ' ', '>', ' ', ' ']
            case 'salary':
                label = [None, ' ', ' ', ' ', ' ', ' ', '>', ' ']
            case 'favorite':
                label = [None, ' ', ' ', ' ', ' ', ' ', ' ', '>']
            case _:
                label = [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        if self.user.sort.get('reverse'):
            label_r = [' ', '>']
        else:
            label_r = ['>', ' ']

        print('<Сортировка>')
        print(f'{label[1]} 1. По сервису\n'
              f'{label[2]} 2. По названию\n'
              f'{label[3]} 3. По дате публикации\n'
              f'{label[4]} 4. По региону\n'
              f'{label[5]} 5. По валюте\n'
              f'{label[6]} 6. По зарплате\n'
              f'{label[7]} 7. Сначала избранные вакансии\n'
              f'{label_r[0]} 8. Отображать с начала\n'
              f'{label_r[1]} 9. Отображать с конца\n'
              '  10. Назад'
              )
        match input('>> '):
            case '1':
                self.sorted['attribute'] = 'service'
                self.user.sort = self.sorted
                self.clear_screen()
                self.menu_sorted_result(source)
            case '2':
                self.sorted['attribute'] = 'title'
                self.user.sort = self.sorted
                self.clear_screen()
                self.menu_sorted_result(source)
            case '3':
                self.sorted['attribute'] = 'date'
                self.user.sort = self.sorted
                self.clear_screen()
                self.menu_sorted_result(source)
            case '4':
                self.sorted['attribute'] = 'area'
                self.user.sort = self.sorted
                self.clear_screen()
                self.menu_sorted_result(source)
            case '5':
                self.sorted['attribute'] = 'currency'
                self.user.sort = self.sorted
                self.clear_screen()
                self.menu_sorted_result(source)
            case '6':
                self.sorted['attribute'] = 'salary'
                self.user.sort = self.sorted
                self.clear_screen()
                self.menu_sorted_result(source)
            case '7':
                self.sorted['attribute'] = 'favorite'
                self.user.sort = self.sorted
                self.clear_screen()
                self.menu_sorted_result(source)
            case '8':
                self.sorted['reverse'] = False
                self.user.sort = self.sorted
                self.clear_screen()
                self.menu_sorted_result(source)
            case '9':
                self.sorted['reverse'] = True
                self.user.sort = self.sorted
                self.clear_screen()
                self.menu_sorted_result(source)
            case '10':
                self.clear_screen()
                self.vacancies.sorted(**self.sorted)
                if source == 'service':
                    self.menu_service_vacancies()
                elif source == 'base':
                    self.menu_base_vacancies()
                else:
                    self.main_menu()
            case _:
                self.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести номер варианта ответа')
                self.menu_base_vacancies()

    def view_result(self, source: str):
        try:
            print(self.vacancies)
        except TypeError:
            pass
        input()
        self.clear_screen()
        if source == 'service':
            self.menu_service_vacancies()
        elif source == 'base':
            self.menu_base_vacancies()
        else:
            self.main_menu()


if __name__ == '__main__':
    ui = TextUI()
    ui.main()
