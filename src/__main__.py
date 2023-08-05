from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI

if __name__ == '__main__':
    hh = HeadHunterAPI()
    hh.get_vacancies('АСУТП', write_json=True)

    sj = SuperJobAPI()
    sj.get_vacancies('АСУТП', write_json=True)

