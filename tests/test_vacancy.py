def test_property(vacancy_1, vacancy_2):
    assert not vacancy_1.is_to_removed
    assert not vacancy_2.is_to_removed


def test_str(vacancy_1, vacancy_2):
    assert str(vacancy_1) == ('Размещено на "HeadHunter" 01.09.2023\n'
                              'Название: Тест vacancy_1\n'
                              'Регион: World\n'
                              'Зарплата: от 1000 до 1000 RUR\n'
                              'Ссылка: https://dev.hh.ru/\n'
                              '\n')

    assert str(vacancy_2) == ('Размещено на "SuperJob" 01.09.2023\n'
                              'Название: Тест vacancy_2\n'
                              'Регион: World\n'
                              'Зарплата: Не указана\n'
                              'Ссылка: https://api.superjob.ru/\n'
                              '\n')
