import os
from pathlib import Path
from dotenv import load_dotenv


# Дирректории
ROOT = Path(__file__).resolve().parent
FIXTURES = Path(ROOT, 'fixtures')

# Файлы
HH_RESPONSE = Path(FIXTURES, 'hh_vacancies.yaml')
SJ_RESPONSE = Path(FIXTURES, 'sj_vacancies.yaml')

# API
load_dotenv()
SJ_KEY = os.getenv('SJ_KEY')  # Секретный ключ для SuperJob
