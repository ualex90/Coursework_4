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
        Инициализируем пользователя из файла если файл есть и содержит имя пользователя
        в противном случае создаем нового пользователя
        :return:
        """
        print('Добро пожаловать в JobParser', end='')
        if Path(USER).exists():
            user = User.init_yaml()
            if user.name:
                print(f', {user.name}!')
                return user
        print('!')
        return User(name=input('Введите свое имя: '))


if __name__ == '__main__':
    ui = TextUI()
    ui.main()
