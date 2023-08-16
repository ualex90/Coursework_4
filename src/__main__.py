from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI

from src.ui.text_ui import TextUI
from src.utils.file_manager import JSONManager
from src.utils.file_manager import YAMLManager
from src.vacancies.vacancies import Vacancies
from src.vacancies.vacancy import Vacancy

if __name__ == '__main__':
    # hh = HeadHunterAPI()  # объект для работы с API HeadHunter
    # sj = SuperJobAPI()  # объект для работы с API HeadHunter
    # vacancies = Vacancies()  # объект для добавления вакансий в список
    # json_manager = JSONManager('test.json')  # объект для сохранения и чтения данных JSON
    # yaml_manager = YAMLManager('test.yaml')  # объект для сохранения и чтения данных YAML
    # hh_source = YAMLManager('hh_source.yaml')  # объект для сохранения исходных данных HH в YAML
    # sj_source = YAMLManager('sj_source.yaml')  # объект для сохранения исходных данных SJ в YAML

    # # Получение вакансий
    # print(hh.get_vacancies('АСУТП', page_limit=1, source=False))
    # print(sj.get_vacancies('АСУТП', page_limit=1, source=False))

    # # Добавление полученных вакансий в список
    # vacancies.add_vacancies(hh.get_vacancies('АСУТП', page_limit=1), log=True)
    # vacancies.add_vacancies(sj.get_vacancies('АСУТП', page_limit=1), log=True)

    # # Сохранение исходных данных в файл
    # hh_source.save(hh.get_vacancies('АСУТП', page_limit=1, source=True))
    # sj_source.save(sj.get_vacancies('АСУТП', page_limit=1, source=True))

    # Сохранение данных о вакансиях в JSON файл
    # json_manager.save_vacancies(vacancies)

    # # Добавление вакансий в список из файла
    # vacancies.add_vacancies(json_manager.load(), log=True)
    # vacancies.sorted('title')

    # Поиск среди названий вакансий
    # result = vacancies.search('junior')
    # [print(i) for i in result]

    # user = yaml_manager.load()

    ui = TextUI()
    ui.main()
