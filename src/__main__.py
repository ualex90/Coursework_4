from src.areas.headhunter_api import HeadHunterAPI

if __name__ == '__main__':
    hh = HeadHunterAPI()
    search_query = {
        'text': 'АСУТП',
        # 'page': 0,
        'per_page': 50
    }
    hh.get_vacancies(**search_query)
    hh.write_json()