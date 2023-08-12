import os
from pathlib import Path

from settings import USER
from src.ui.ui import UI
from src.user.user import User


class TextUI(UI):
    def main(self):
        self.user = self.get_user()

    def get_user(self) -> User:
        print('Добро пожаловать в JobParser', end='')
        if Path(USER).exists():
            user = User.init_yaml()
            if user.name:
                print(f', {user.name}!')
                return user
        print('!')
        return User(**{'name': input('Введите свое имя: ')})


if __name__ == '__main__':
    ui = TextUI()
    ui.main()
