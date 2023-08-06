import pytest


@pytest.mark.parametrize('in_area, in_date, salary,'
                         'out_area, out_date, out_salary_from, out_salary_to, out_currency',
                         [({'name': 'World'}, '2023-08-01T18:29:46+0300', {'from': 1000, 'to': 1000, 'currency': 'RUR'},
                           'World', '01.08.2023', 1000, 1000, 'RUR'),
                          ({'name': 'W, in'}, '2023-08-01T18:29:46+0300', {'from': 1000, 'to': 1000, 'currency': 'RUR'},
                           'W', '01.08.2023', 1000, 1000, 'RUR'),
                          (None, '2023-08-01T18:29:46+0300', {'from': 1000, 'to': 1000, 'currency': 'RUR'},
                           'None', '01.08.2023', 1000, 1000, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': 1000, 'to': 1000, 'currency': 'RUR'},
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': 100, 'to': 1000, 'currency': 'RUR'},
                           'World', '01.01.2024', 100, 1000, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': 1000, 'to': 100, 'currency': 'RUR'},
                           'World', '01.01.2024', 1000, 100, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': 1000, 'to': 0, 'currency': 'RUR'},
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': 1000, 'to': None, 'currency': 'RUR'},
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': 0, 'to': 1000, 'currency': 'RUR'},
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': None, 'to': 1000, 'currency': 'RUR'},
                           'World', '01.01.2024', 1000, 1000, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': 0, 'to': 0, 'currency': 'RUR'},
                           'World', '01.01.2024', 0, 0, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': None, 'to': None, 'currency': 'RUR'},
                           'World', '01.01.2024', 0, 0, 'RUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': 1000, 'to': 1000, 'currency': 'EUR'},
                           'World', '01.01.2024', 1000, 1000, 'EUR'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', {'from': 1000, 'to': 1000, 'currency': None},
                           'World', '01.01.2024', 1000, 1000, 'None'),
                          ({'name': 'World'}, '2024-01-01T00:00:00+0000', None,
                           'World', '01.01.2024', 0, 0, 'None'),
                          ])
def test_normalization_data(hh, in_area, in_date, salary,
                            out_area, out_date, out_salary_from, out_salary_to, out_currency):
    in_data = ([{'id': '1111',
                 'area': in_area,
                 'name': 'Тест метода нормализации данных',
                 'published_at': in_date,
                 'salary': salary,
                 'alternate_url': 'https://dev.hh.ru/'
                 }])
    out_data = hh.normalization_data(in_data)
    assert out_data == ([{'service': 'HeadHunter',
                          'vacancy_id': 1111,
                          'name': 'Тест метода нормализации данных',
                          'date': out_date,
                          'area': out_area,
                          'currency': out_currency,
                          'salary_fom': out_salary_from,
                          'salary_to': out_salary_to,
                          'url': 'https://dev.hh.ru/'
                          }])
