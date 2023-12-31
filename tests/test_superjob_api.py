import pytest


@pytest.mark.parametrize('in_area, in_date, in_salary_from, in_salary_to, currency,'
                         'out_area, out_date, out_salary_from, out_salary_to, out_currency',
                         [('World', 1693576576, 1000, 1000, 'rub',
                           'World', '01.09.2023', 1000, 1000, 'RUR'),
                          ('W, in', 1693576576, 1000, 1000, 'rub',
                           'W', '01.09.2023', 1000, 1000, 'RUR'),
                          (None, 1693576576, 1000, 1000, 'rub',
                           'None', '01.09.2023', 1000, 1000, 'RUR'),
                          ('World', 1704031200, 1000, 1000, 'rub',
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ('World', 1704031200, 100, 1000, 'rub',
                           'World', '01.01.2024', 100, 1000, 'RUR'),
                          ('World', 1704031200, 1000, 100, 'rub',
                           'World', '01.01.2024', 1000, 100, 'RUR'),
                          ('World', 1704031200, 1000, 0, 'rub',
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ('World', 1704031200, 1000, None, 'rub',
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ('World', 1704031200, 0, 1000, 'rub',
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ('World', 1704031200, None, 1000, 'rub',
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ('World', 1704031200, 0, 0, 'rub',
                           'World', '01.01.2024', 0, 0, 'RUR'),
                          ('World', 1704031200, None, None, 'rub',
                           'World', '01.01.2024', 0, 0, 'RUR'),
                          ('World', 1704031200, 1000, 1000, 'eur',
                           'World', '01.01.2024', 1000, 1000, 'EUR'),
                          ('World', 1704031200, 1000, 1000, None,
                           'World', '01.01.2024', 1000, 1000, 'None'),
                          ])
def test_normalization_data(sj, in_area, in_date, currency, in_salary_from, in_salary_to,
                            out_area, out_date, out_salary_from, out_salary_to, out_currency):
    in_data = ([{'id': '1111',
                 'address': in_area,
                 'profession': 'Тест метода нормализации данных',
                 'date_published': in_date,
                 'currency': currency,
                 'payment_from': in_salary_from,
                 'payment_to': in_salary_to,
                 'link': 'https://api.superjob.ru/'
                 }])
    out_data = sj.normalization_data(in_data)
    assert out_data == {'SJ_1111': {'service': 'SuperJob',
                                    'title': 'Тест метода нормализации данных',
                                    'date': out_date,
                                    'area': out_area,
                                    'currency': out_currency,
                                    'salary_fom': out_salary_from,
                                    'salary_to': out_salary_to,
                                    'url': 'https://api.superjob.ru/'
                                    }}
