import os
from pathlib import Path
from dotenv import load_dotenv


# Дирректории
ROOT = Path(__file__).resolve().parent
FIXTURES = Path(ROOT, 'fixtures')
CONFIG = Path(ROOT, 'config')

# Файлы
HH_SOURCE = Path(FIXTURES, 'hh_source.yaml')  # Исходные джанные с SJ
SJ_SOURCE = Path(FIXTURES, 'sj_source.yaml')  # Исходные джанные с SJ
CONFIG_FILE = Path(CONFIG, 'config.yaml')  # Настройки программы
USER_FILE = Path(CONFIG, 'user.yaml')  # Пользовательские настройки
# API
load_dotenv()
SJ_KEY = os.getenv('SJ_KEY')  # Секретный ключ для SuperJob
