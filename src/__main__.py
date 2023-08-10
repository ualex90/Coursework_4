from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI
from src.utils.jsonsaver import JSONSaver
from src.vacancies.vacancies import Vacancies
from src.vacancies.vacancy import Vacancy

if __name__ == '__main__':
    hh = HeadHunterAPI()  # объект для работы с API HeadHunter
    sj = SuperJobAPI()  # объект для работы с API HeadHunter
    vacancies = Vacancies()  # объект для добавления вакансий в список
    json_saver = JSONSaver('test.json')  # объект для сохранения и чтения вакансий из файла

    # # Получение вакансий
    # print(hh.get_vacancies('АСУТП', page_limit=2, write_json=False))
    # print(sj.get_vacancies('АСУТП', page_limit=1, write_json=False))

    # # Добавление полученных вакансий в список
    # vacancies.add_vacancies(hh.get_vacancies('АСУТП', page_limit=2), log=True)
    # vacancies.add_vacancies(sj.get_vacancies('АСУТП', page_limit=1), log=True)
    #
    # # Сохранение данных в JSON файл
    # json_saver.save(vacancies)

    # Добавление вакансий в список из файла
    vacancies.add_vacancies(json_saver.load(), log=True)
    print(vacancies.list)
