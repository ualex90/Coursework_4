from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI

if __name__ == '__main__':
    hh = HeadHunterAPI()
    sj = SuperJobAPI()

    # hh.get_vacancies('АСУТП', write_json=True)
    # sj.get_vacancies('АСУТП', write_json=True)

    hh.get_vacancies('АСУТП')
    sj.get_vacancies('АСУТП')

    # print(sj.get_vacancies('АСУТП'))
    # print(hh.get_vacancies('АСУТП'))

