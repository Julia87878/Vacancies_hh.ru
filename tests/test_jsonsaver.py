import json
from unittest.mock import Mock, patch

from src.jsonsaver import JSONSaver


def test_get_data_from_file(test_path_1):
    jsonsaver_1 = JSONSaver(test_path_1)
    result = jsonsaver_1.get_data_from_file()
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
    ]
    assert result == expected


def test_get_data_from_file_decode_error(test_path_2):
    jsonsaver_2 = JSONSaver(test_path_2)
    result = jsonsaver_2.get_data_from_file()
    expected = []
    assert result == expected


class TestJSONSaver:
    """Класс для тестирования JSONSaver"""

    @patch("src.jsonsaver.JSONSaver.get_data_from_file")
    def test_add_data_in_file(self, mock_get_data_from_file: Mock, vacancies_list_10: list, test_path_3) -> None:
        mock_get_data_from_file.return_value = []
        json_saver_3 = JSONSaver(test_path_3)
        json_saver_3.add_data_in_file(vacancies_list_10)
        with open(test_path_3, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data == vacancies_list_10

    @patch("src.jsonsaver.JSONSaver.get_data_from_file")
    def test_delete_data_from_file(self, mock_get_data_from_file: Mock, vacancies_list_10: list, test_path_4) -> None:
        mock_get_data_from_file.return_value = vacancies_list_10
        json_saver_4 = JSONSaver(test_path_4)
        url = "https://api.hh.ru/vacancies/111986438?host=hh.ru"
        json_saver_4.delete_data_from_file(url)
        with open(test_path_4, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert data == [
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
