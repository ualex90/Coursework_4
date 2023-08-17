import os
import time
from pathlib import Path

from settings import USER
from src.user.user import User
from src.utils.file_manager import JSONManager
from src.vacancies.vacancy import Vacancy


class UIUtils:
    def __init__(self) -> None:
        self.operating_system = os.name
        self.is_changed = False

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

    def view_vacancy(self, item: Vacancy) -> None:
        self.clear_screen()
        print(item)
        print('==========================\n'
              'Нажмите ENTER для возврата\n'
              '(d): отметь/снять отметку - к удалению\n'
              '(f): отметь/снять отметку - избранное'
              )
        match input('>> '):
            case 'd':
                if item.is_to_removed:
                    item.is_to_removed = False
                else:
                    item.is_to_removed = True
            case 'f':
                if item.is_favorite:
                    item.is_favorite = False
                else:
                    item.is_favorite = True
        self.clear_screen()
