from pathlib import Path


# Дирректории
ROOT = Path(__file__).resolve().parent
FIXTURES = Path(ROOT, 'fixtures')

# Файлы
HH_VACANCIES = Path(FIXTURES, 'hh_vacancies.json')
SJ_VACANCIES = Path(FIXTURES, 'sj_vacancies.json')
