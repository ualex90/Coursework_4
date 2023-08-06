from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI
from src.vacancies.vacancy import Vacancy

if __name__ == '__main__':
    hh = HeadHunterAPI()
    sj = SuperJobAPI()

    # hh.get_vacancies('АСУТП', write_json=True)

    # hh.get_vacancies('АСУТП')
    # sj.get_vacancies('АСУТП')

    # print(sj.get_vacancies('АСУТП'))

    for item in hh.get_vacancies('АСУТП'):
        print(Vacancy(**item))
