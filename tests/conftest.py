import pytest

from src import settings
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1() -> Vacancy:
    return Vacancy(
        "Тестировщик ПО/QA",
        80000,
        "Знания SQL, python. Опыт тестирования",
        "https://api.hh.ru/vacancies/117253650?host=hh.ru",
    )


@pytest.fixture
def vacancy_2() -> Vacancy:
    return Vacancy("Разработчик", 100000, "Знание python.", "https://api.hh.ru/vacancies/117253640?host=hh.ru")


@pytest.fixture
def vacancy_3() -> Vacancy:
    return Vacancy("Python-Разработчик", 100000, "Знание python.", "https://api.hh.ru/vacancies/117253630?host=hh.ru")


@pytest.fixture
def vacancy_7() -> dict:
    return {
        "name": "Инженер-программист junior",
        "salary": {"from": 110000, "to": None, "currency": "RUR"},
        "url": "https://api.hh.ru/vacancies/111986458?host=hh.ru",
        "snippet": {"requirement": "Опыт программирования на любом из языков ООП"},
    }


@pytest.fixture
def vacancy_object() -> Vacancy:
    return Vacancy("Разработчик", 100000, "Знание Python", "https://api.hh.ru/vacancies/108168117?host=hh.ru")


@pytest.fixture
def hh_api_vacancies_list() -> list:
    return [
        {
            "name": "Python-Разработчик",
            "salary": {"from": 150000, "to": None, "currency": "RUR"},
            "url": "https://api.hh.ru/vacancies/11198638?host=hh.ru",
            "snippet": {"requirement": "Опыт разработки на Python."},
        },
        {
            "name": "Python junior",
            "salary": {"from": 100000, "to": None, "currency": "RUR"},
            "url": "https://api.hh.ru/vacancies/111986448?host=hh.ru",
            "snippet": {"requirement": "Знание Python, SQL."},
        },
        {
            "name": "Python senior",
            "salary": "Не указана",
            "url": "https://api.hh.ru/vacancies/111986458?host=hh.ru",
            "snippet": {"requirement": "Опыт программирования на Python."},
        },
    ]


@pytest.fixture
def vacancies_list_10() -> list:
    return [
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
        {
            "name": "Java junior",
            "salary_from": 80000,
            "snippet": "Знание Java, SQL.",
            "url": "https://api.hh.ru/vacancies/111986428?host=hh.ru",
        },
        {
            "name": "Python senior",
            "salary_from": 120000,
            "snippet": "Опыт программирования на Python.",
            "url": "https://api.hh.ru/vacancies/111986478?host=hh.ru",
        },
        {
            "name": "Java Разработчик",
            "salary_from": "Не указана",
            "snippet": "Опыт программирования на Java.",
            "url": "https://api.hh.ru/vacancies/111986498?host=hh.ru",
        },
    ]


@pytest.fixture
def vacancies_list_2() -> list:
    return [
        {
            "name": "Python junior",
            "salary_from": 700000,
            "snippet": "Опыт на Python. ",
            "url": "https://api.hh.ru/vacancies/111986414?host=hh.ru",
        },
        {
            "name": "Java junior",
            "salary_from": 800000,
            "snippet": "Опыт на Java.",
            "url": "https://api.hh.ru/vacancies/111986415?host=hh.ru",
        },
    ]


@pytest.fixture
def test_path_1():
    path_to_file = settings.BASE_DIR.joinpath("data", "test_vacancies_1.json")
    return path_to_file


@pytest.fixture
def test_path_2():
    path_to_file = settings.BASE_DIR.joinpath("data", "test_vacancies_2.json")
    return path_to_file


@pytest.fixture
def test_path_3():
    path_to_file = settings.BASE_DIR.joinpath("data", "test_vacancies_3.json")
    return path_to_file


@pytest.fixture
def test_path_4():
    path_to_file = settings.BASE_DIR.joinpath("data", "test_vacancies_4.json")
    return path_to_file
