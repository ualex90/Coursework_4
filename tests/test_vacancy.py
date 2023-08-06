def test_str(vacancy_1, vacancy_2):
    assert str(vacancy_1) == f'''Название: "Тест vacancy_1"
Регион: World
Зарплата: 1000 RUR
Ссылка: https://dev.hh.ru/
'''
    assert str(vacancy_2) == f'''Название: "Тест vacancy_2"
Регион: World
Зарплата: Не указана
Ссылка: https://api.superjob.ru/
'''
