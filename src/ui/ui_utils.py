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
        self.conf = ConfigTool.init_yaml()  # Настройки программы
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
        label = [' ' for i in range(9)]
        label[1] = f'   >' if self.conf.is_hh_source else '    '
        label[2] = f'   >' if self.conf.is_sj_source else '    '
        label[3] = f'   >' if self.conf.is_vacancies_log else '    '
        label[4] = f'   >' if self.conf.is_save_log else '    '
        label[5] = f'({self.conf.hh_limit:<2})' if self.conf.hh_limit else '(40)'
        label[6] = f' ({self.conf.sj_limit:<1})' if self.conf.sj_limit else ' (6)'
        label[7] = f'   !'
        label[8] = f'   !'

        print('<Выбор сервиса поска работы>')
        print(f'{label[1]} 1. Сохранять исходные данные HeadHunter\n'
              f'{label[2]} 2. Сохранять исходные данные SuperJob\n'
              f'{label[3]} 3. Отображать лог добавления вакансий в список\n'
              f'{label[4]} 4. Отображать лог сохранения в файл\n'
              f'{label[5]} 5. Лимит запроса страниц HeadHunter (не более 40)\n'
              f'{label[6]} 6. Лимит запроса страниц SuperJob (не более 6)\n'
              f'{label[7]} 7. Очистить локальную базу данных\n'
              f'{label[8]} 8. Удалить пользователя\n'
              f'     9. Назад, в главное меню'
              )
        match input('>> ').strip():
            case '1':
                self.conf.is_hh_source = False if self.conf.is_hh_source else True
                self.clear_screen()
                self.settings()
            case '2':
                self.conf.is_sj_source = False if self.conf.is_sj_source else True
                self.clear_screen()
                self.settings()
            case '3':
                self.conf.is_vacancies_log = False if self.conf.is_vacancies_log else True
                self.clear_screen()
                self.settings()
            case '4':
                self.conf.is_save_log = False if self.conf.is_save_log else True
                self.clear_screen()
                self.settings()
            case '5':
                self.clear_screen()
                self.settings()
            case '6':
                self.clear_screen()
                self.settings()
            case '7':
                self.clear_screen()
                self.settings()
            case '8':
                self.clear_screen()
                self.settings()
            case '9':
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
