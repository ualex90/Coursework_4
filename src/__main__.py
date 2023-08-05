from src.api.headhunter_api import HeadHunterAPI

if __name__ == '__main__':
    hh = HeadHunterAPI()
    hh.get_vacancies('инженер')
    hh.write_json()
