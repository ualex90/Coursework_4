from src.vacancies.vacancy import Vacancy


def test_add_vacancies(vacancies, vacancies_dict_1, vacancies_dict_2, vacancies_dict_3):
    assert len(vacancies.list) == 0
    vacancies.add_vacancies(vacancies_dict_1)
    assert len(vacancies.list) == 1
    assert isinstance(vacancies.list[0], Vacancy)
    vacancies.add_vacancies(vacancies_dict_2)
    assert len(vacancies.list) == 3
    vacancies.add_vacancies(vacancies_dict_3)
    assert len(vacancies.list) == 6
    assert isinstance(vacancies.list[5], Vacancy)
    assert vacancies.list[0].vacancy_id == 'HH_0001'
    assert vacancies.list[1].vacancy_id == 'HH_0002'
    assert vacancies.list[2].vacancy_id == 'SJ_0001'
    assert vacancies.list[3].vacancy_id == 'HH_0003'
    assert vacancies.list[4].vacancy_id == 'SJ_0002'
    assert vacancies.list[5].vacancy_id == 'SJ_0003'

