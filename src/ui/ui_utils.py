import os
import time
from pathlib import Path

from settings import USER_FILE
from src.config.config_tool import ConfigTool
from src.config.user import User
from src.vacancies.vacancy import Vacancy


class UIUtils:
    def __init__(self) -> None:
        self.operating_system = os.name  # Тип операционной системы
        self.is_changed = False  # Флаг изменения меток

    def clear_screen(self) -> None:
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
        if Path(USER_FILE).exists():
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

    def settings(self) -> None:
        """Выбор сервиса поиска работы"""
        label = [' ' for i in range(5)]

        # match self.config.service:
        #     case 1:
        #         label = [None, '>', ' ', ' ']
        #     case 2:
        #         label = [None, ' ', '>', ' ']
        #     case 3:
        #         label = [None, ' ', ' ', '>']
        #     case _:
        #         label = [None, ' ', ' ', ' ']

        print('<Выбор сервиса поска работы>')
        print(f'{label[1]} 1. Сохранять полученные данные с сервисов\n'
              f'{label[2]} 2. HeadHunter\n'
              f'{label[3]} 3. SuperJob\n'
              f'  4. Назад, в главное меню'
              )
        match input('>> ').strip():
            case '1':
                self.clear_screen()
                self.settings()
            case '2':
                self.clear_screen()
                self.settings()
            case '3':
                self.clear_screen()
                self.settings()
            case '4':
                self.clear_screen()
                return None
            case _:
                self.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести номер варианта ответа')
                self.settings()

    def view_vacancy(self, item: Vacancy) -> None:
        self.clear_screen()
        print(item)
        print('==========================\n'
              'Нажмите ENTER для возврата\n'
              '(d): отметь/снять метку - к удалению\n'
              '(f): отметь/снять метку - избранное'
              )
        match input('>> '):
            case 'd':
                self.is_changed = True
                if item.is_to_removed:
                    item.is_to_removed = False
                else:
                    item.is_to_removed = True
            case 'f':
                self.is_changed = True
                if item.is_favorite:
                    item.is_favorite = False
                else:
                    item.is_favorite = True
        self.clear_screen()
