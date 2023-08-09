from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI
from src.utils.jsonsaver import JSONSaver
from src.vacancies.vacancies import Vacancies
from src.vacancies.vacancy import Vacancy

if __name__ == '__main__':
    hh = HeadHunterAPI()
    sj = SuperJobAPI()

    # hh.get_vacancies('АСУТП', write_json=True)

    # hh.get_vacancies('АСУТП')
    # sj.get_vacancies('АСУТП')

    # print(hh.get_vacancies('АСУТП', page_limit=2))
    # print(sj.get_vacancies('АСУТП'))

    # for item in hh.get_vacancies('Python', page_limit=2, write_json=True):
    #     print(Vacancy(item))
    # for item in sj.get_vacancies('АСУТП', write_json=True):
    #     print(Vacancy(item))

    vacancies = Vacancies()
    json_saver = JSONSaver('test.json')
    # vacancies.add_vacancies(hh.get_vacancies('АСУТП', page_limit=2), log=True)
    # vacancies.add_vacancies(sj.get_vacancies('АСУТП', page_limit=1), log=True)
    # json_saver.save(vacancies)
    vacancies.add_vacancies(json_saver.load(), log=True)

