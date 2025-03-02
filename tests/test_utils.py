from src.utils import get_top_n_vacancies, get_vacancies_by_keyword, get_vacancies_salary_from, to_str


def test_get_vacancies_by_keyword(vacancies_list_10):
    result = get_vacancies_by_keyword(vacancies_list_10, "Python")
    expected = [
        {
            "name": "Python-Разработчик",
            "salary_from": 150000,
            "snippet": "Опыт разработки на Python.",
            "url": "https://api.hh.ru/vacancies/111986438?host=hh.ru",
        },
        {
            "name": "Python junior",
            "salary_from": 100000,
            "snippet": "Знание Python, SQL.",
            "url": "https://api.hh.ru/vacancies/111986448?host=hh.ru",
        },
        {
            "name": "Python senior",
            "salary_from": 200000,
            "snippet": "Опыт разработки на Python. Знание Java, SQL.",
            "url": "https://api.hh.ru/vacancies/111986414?host=hh.ru",
        },
        {
            "name": "Python-Разработчик",
            "salary_from": 150000,
            "snippet": "Опыт разработки на Python.",
            "url": "https://api.hh.ru/vacancies/111986435?host=hh.ru",
        },
        {
            "name": "Python junior",
            "salary_from": 80000,
            "snippet": "Знание Python, SQL.",
            "url": "https://api.hh.ru/vacancies/111986425?host=hh.ru",
        },
        {
            "name": "Python-Разработчик",
            "salary_from": 150000,
            "snippet": "Опыт разработки на Python.",
            "url": "https://api.hh.ru/vacancies/111986418?host=hh.ru",
        },
        {
            "name": "Python senior",
            "salary_from": 120000,
            "snippet": "Опыт программирования на Python.",
            "url": "https://api.hh.ru/vacancies/111986478?host=hh.ru",
        },
    ]
    assert result == expected


def test_get_vacancies_salary_from(vacancies_list_10):
    result = get_vacancies_salary_from(150000, vacancies_list_10)
    expected = [
        {
            "name": "Python-Разработчик",
            "salary_from": 150000,
            "snippet": "Опыт разработки на Python.",
            "url": "https://api.hh.ru/vacancies/111986438?host=hh.ru",
        },
        {
            "name": "Python senior",
            "salary_from": 200000,
            "snippet": "Опыт разработки на Python. Знание Java, SQL.",
            "url": "https://api.hh.ru/vacancies/111986414?host=hh.ru",
        },
        {
            "name": "Python-Разработчик",
            "salary_from": 150000,
            "snippet": "Опыт разработки на Python.",
            "url": "https://api.hh.ru/vacancies/111986435?host=hh.ru",
        },
        {
            "name": "Java senior",
            "salary_from": 170000,
            "snippet": "Опыт программирования на Java.",
            "url": "https://api.hh.ru/vacancies/111986415?host=hh.ru",
        },
        {
            "name": "Python-Разработчик",
            "salary_from": 150000,
            "snippet": "Опыт разработки на Python.",
            "url": "https://api.hh.ru/vacancies/111986418?host=hh.ru",
        },
    ]
    assert result == expected


def test_get_top_n_vacancies(vacancies_list_10):
    result = get_top_n_vacancies(vacancies_list_10, 3)
    expected = [
        {
            "name": "Python senior",
            "salary_from": 200000,
            "snippet": "Опыт разработки на Python. Знание Java, " "SQL.",
            "url": "https://api.hh.ru/vacancies/111986414?host=hh.ru",
        },
        {
            "name": "Java senior",
            "salary_from": 170000,
            "snippet": "Опыт программирования на Java.",
            "url": "https://api.hh.ru/vacancies/111986415?host=hh.ru",
        },
        {
            "name": "Python-Разработчик",
            "salary_from": 150000,
            "snippet": "Опыт разработки на Python.",
            "url": "https://api.hh.ru/vacancies/111986438?host=hh.ru",
        },
    ]
    assert result == expected


def test_to_str(vacancies_list_2):
    result = to_str(vacancies_list_2)
    expected = (
        "Название вакансии: Python junior, Зарплата: от 700000, Требования: Опыт на Python. , "
        "Ссылка на вакансию: https://api.hh.ru/vacancies/111986414?host=hh.ru. Название вакансии: Java junior, "
        "Зарплата: от 800000, Требования: Опыт на Java., "
        "Ссылка на вакансию: https://api.hh.ru/vacancies/111986415?host=hh.ru."
    )
    assert result == expected
