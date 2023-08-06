def test_add_vacancies(vacancies, vacancies_list_1, vacancies_list_2, vacancies_list_3):
    assert len(vacancies.vacancies) == 0
    vacancies.add_vacancies(vacancies_list_1)
    assert len(vacancies.vacancies) == 1
    vacancies.add_vacancies(vacancies_list_2)
    assert len(vacancies.vacancies) == 3
    vacancies.add_vacancies(vacancies_list_3)
    assert len(vacancies.vacancies) == 6
