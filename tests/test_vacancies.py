def test_add_vacancies(vacancies, vacancies_list_1, vacancies_list_2, vacancies_list_3):
    assert len(vacancies.data) == 0
    vacancies.add_vacancies(vacancies_list_1)
    assert len(vacancies.data) == 1
    vacancies.add_vacancies(vacancies_list_2)
    assert len(vacancies.data) == 3
    vacancies.add_vacancies(vacancies_list_3)
    assert len(vacancies.data) == 6
