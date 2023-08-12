from pathlib import Path

from settings import USER
from src.ui.ui import UI
from src.user.user import User


class TextUI(UI):
    """Пользовательский интерфейс"""
    def main(self):
        """главный диалог"""
        self.user = self.get_user()

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


if __name__ == '__main__':
    ui = TextUI()
    ui.main()
