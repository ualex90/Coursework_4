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
USER = Path(CONFIG, 'user.yaml')  # Данные о пользователе
# API
load_dotenv()
SJ_KEY = os.getenv('SJ_KEY')  # Секретный ключ для SuperJob
