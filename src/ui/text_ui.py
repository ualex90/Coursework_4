from pathlib import Path

from settings import USER
from src.ui.ui import UI
from src.user.user import User


class TextUI(UI):
    """Пользовательский интерфейс"""

    def main(self):
        """главный метод UI"""
        self.user = self.get_user()
        self.main_menu()

    def get_user(self) -> User:
        """
        Инициализируем пользователя из файла, если файл есть и содержит имя пользователя
        в противном случае - создаем нового пользователя
        :return:
        """
        greetings = 'Добро пожаловать в JobParser'
        print(greetings, end='')
        if Path(USER).exists():
            user = User.init_yaml()
            if user.name:
                print(f', {user.name}!')
                print('-' * (len(greetings) + len(user.name) + 3), '\n')
                return user
        print('!')
        user = User(name=input('Введите свое имя: '))
        print('-' * (len(greetings) + 1), '\n')
        return user

    def main_menu(self):
        print('<Что будем делать?>')
        print('1. Настраивать параметры программы\n'
              '2. Искать вакансий на выбранных площадках\n'
              '3. Искать в сохраненной базе данных')


if __name__ == '__main__':
    ui = TextUI()
    ui.main()
