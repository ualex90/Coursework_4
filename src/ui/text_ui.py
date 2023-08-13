import os
import time
from pathlib import Path

from settings import USER
from src.ui.ui import UI
from src.user.user import User
from src.vacancies import vacancies


class TextUI(UI):
    """Пользовательский интерфейс"""

    def main(self):
        """главный метод UI"""
        self.user = self.get_user()
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
              '3. Найти вакансии в сохраненной базе данных\n'
              '4. Настроить программу\n'
              '5. Выход из программы')
        match input('>> '):
            case '1':
                self.clear_screen()
                self.search_settings()
            case '2':
                self.clear_screen()
                self.search_in_service()
            case '3':
                pass
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
        """Выбор сервиса поска работы"""
        if self.user.service == 1:
            label = [None, '>', ' ', ' ']
        elif self.user.service == 2:
            label = [None, ' ', '>', ' ']
        elif self.user.service == 3:
            label = [None, ' ', ' ', '>']
        else:
            label = [None, ' ', ' ', ' ']

        print('<Выбор сервиса поска работы>')
        print(f'{label[1]} 1. SuperJob + HeadHunter\n'
              f'{label[2]} 2. HeadHunter\n'
              f'{label[3]} 3. SuperJob\n'
              f'  4. Назад, в главное меню')
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
        print('<Поиск работы на сервисах>')
        print('Для выхода в главное меню, введите "exit"\n'
              'Введите название вакансии:')
        if (request := input('>> ').lower().strip()) == 'exit':
            self.clear_screen()
            self.main_menu()
        else:
            match self.user.service:
                case 1:
                    self.clear_screen()
                    self.vacancies.add_vacancies(self.hh.get_vacancies(request, page_limit=4), log=True)
                case 2:
                    self.clear_screen()
                    self.vacancies.add_vacancies(self.hh.get_vacancies(request, page_limit=4), log=True)
                case 3:
                    self.clear_screen()
                    self.vacancies.add_vacancies(self.sj.get_vacancies(request, page_limit=4), log=True)




if __name__ == '__main__':
    ui = TextUI()
    ui.main()
