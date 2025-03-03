import pytest

from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    assert vacancy_1.name == "Тестировщик ПО/QA"
    assert vacancy_1.salary_from == 80000
    assert vacancy_1.snippet == "Знания SQL, python. Опыт тестирования"
    assert vacancy_1.url == "https://api.hh.ru/vacancies/117253650?host=hh.ru"


def test_gt(vacancy_2, vacancy_1):
    assert vacancy_2.salary_from > vacancy_1.salary_from


def test_ge(vacancy_2, vacancy_3):
    assert vacancy_2.salary_from >= vacancy_3.salary_from


def test_lt(vacancy_1, vacancy_2):
    assert vacancy_1.salary_from < vacancy_2.salary_from


def test_le(vacancy_1, vacancy_2):
    assert vacancy_1.salary_from <= vacancy_2.salary_from


def test_le_2(vacancy_2, vacancy_3):
    assert vacancy_2.salary_from <= vacancy_3.salary_from


def test_cast_to_object_list(hh_api_vacancies_list):
    result = Vacancy.cast_to_object_list(hh_api_vacancies_list)
    expected = [
        {
            "name": "Python-Разработчик",
            "salary_from": 150000,
            "snippet": "Опыт разработки на Python.",
            "url": "https://api.hh.ru/vacancies/11198638?host=hh.ru",
        },
        {
            "name": "Python junior",
            "salary_from": 100000,
            "snippet": "Знание Python, SQL.",
            "url": "https://api.hh.ru/vacancies/111986448?host=hh.ru",
        },
        {
            "name": "Python senior",
            "salary_from": "Зарплата не указана.",
            "snippet": "Опыт программирования на Python.",
            "url": "https://api.hh.ru/vacancies/111986458?host=hh.ru",
        },
    ]
    assert result == expected


def test_to_dict(vacancy_3):
    result = vacancy_3.to_dict()
    expected = {
        "name": "Python-Разработчик",
        "salary_from": 100000,
        "snippet": "Знание python.",
        "url": "https://api.hh.ru/vacancies/117253630?host=hh.ru",
    }
    assert result == expected


class TestVacancy:
    """Класс для тестирования Vacancy"""

    def test_str(self, vacancy_object: Vacancy) -> None:
        result = vacancy_object.__str__()
        expected = (
            "Название вакансии: Разработчик, Зарплата: от 100000, Требования: Знание Python, "
            "Ссылка на вакансию: https://api.hh.ru/vacancies/108168117?host=hh.ru."
        )
        assert result == expected

    @staticmethod
    def test___validate_name(vacancy_object: Vacancy) -> None:
        """Корректная работа валидации названия вакансии"""
        result = vacancy_object._Vacancy__validate_name(name="")
        assert result == "Название вакансии не указано."
        result = vacancy_object._Vacancy__validate_name(name="Разработчик")
        assert result == "Разработчик"

    @staticmethod
    def test___validate_salary(vacancy_object: Vacancy) -> None:
        """Корректная работа валидации зарплаты"""
        result = vacancy_object._Vacancy__validate_salary(salary="")
        assert result == "Зарплата не указана."
        result = vacancy_object._Vacancy__validate_salary(salary="по договоренности")
        assert result == "Зарплата не указана."
        result = vacancy_object._Vacancy__validate_salary(salary=100000)
        assert result == 100000
        with pytest.raises(ValueError):
            vacancy_object._Vacancy__validate_salary(salary=-7)

    @staticmethod
    def test___validate_snippet(vacancy_object: Vacancy) -> None:
        """Корректная работа валидации требований к соискателю"""
        result = vacancy_object._Vacancy__validate_snippet(snippet="")
        assert result == "Требования к соискателю не указаны."
        result = vacancy_object._Vacancy__validate_snippet(snippet="Знание Python")
        assert result == "Знание Python"

    @staticmethod
    def test___validate_url(vacancy_object: Vacancy) -> None:
        """Корректная работа валидации ссылки на вакансию"""
        result = vacancy_object._Vacancy__validate_url(url="")
        assert result == "Ссылка на вакансию не указана."
        result = vacancy_object._Vacancy__validate_url(url="https://api.hh.ru/vacancies/108168117?host=hh.ru")
        assert result == "https://api.hh.ru/vacancies/108168117?host=hh.ru"
