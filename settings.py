import os
from pathlib import Path
from dotenv import load_dotenv


# Дирректории
ROOT = Path(__file__).resolve().parent
FIXTURES = Path(ROOT, 'fixtures')

# Файлы
HH_VACANCIES = Path(FIXTURES, 'hh_vacancies.json')
SJ_VACANCIES = Path(FIXTURES, 'sj_vacancies.json')

# API
load_dotenv()
SJ_KEY = os.getenv('SJ_KEY')  # Секретный ключ для SuperJob
