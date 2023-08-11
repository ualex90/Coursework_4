def test_property(vacancy_1, vacancy_2):
    # Test case # 1
    assert not vacancy_1.is_favorite
    assert vacancy_2.is_favorite
    assert not vacancy_1.is_to_removed
    assert not vacancy_2.is_to_removed
    # Test case # 2
    vacancy_1.is_favorite = 'Ok'
    assert not vacancy_1.is_favorite
    vacancy_1.is_favorite = True
    assert vacancy_1.is_favorite
    vacancy_2.is_to_removed = 'Ok'
    assert not vacancy_2.is_to_removed
    vacancy_2.is_to_removed = True
    assert vacancy_2.is_to_removed
    vacancy_2.is_favorite = False
    assert not vacancy_2.is_favorite


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
