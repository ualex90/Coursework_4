from src.api.headhunter_api import HeadHunterAPI
from src.api.superjob_api import SuperJobAPI

if __name__ == '__main__':
    # hh = HeadHunterAPI()
    # hh.get_vacancies('АСУТП')
    # hh.write_json()

    sj = SuperJobAPI()
    sj.get_vacancies('Python')
    sj.write_json()
