from unittest.mock import Mock, patch

import pytest

from src.headhunterapi import HeadHunterAPI

hh = HeadHunterAPI()


@patch("src.headhunterapi.requests.get")
def test__connect_to_api_error(mocked_get):
    response = Mock(status_code=400)
    mocked_get.return_value = response

    with pytest.raises(ValueError):
        hh._connect_to_api()


@patch("src.headhunterapi.requests.get")
def test__connect_to_api_successful(mocked_get):
    response = Mock(status_code=200)
    response.json.return_value = {
        "items": [
            {
                "name": "Тестировщик ПО/QA",
                "salary_from": 80000,
                "snippet": "Знание принципов ручного тестирования. Знания по работе"
                " с консолью <highlighttext>разработчика</highlighttext> в браузере."
                " Знания SQL, python. Опыт тестирования веб и/или...",
                "url": "https://api.hh.ru/vacancies/117253650?host=hh.ru",
            }
        ]
    }
    mocked_get.return_value = response
    result = hh._connect_to_api()
    assert result == {
        "items": [
            {
                "name": "Тестировщик ПО/QA",
                "salary_from": 80000,
                "snippet": "Знание принципов ручного тестирования. Знания по работе"
                " с консолью <highlighttext>разработчика</highlighttext> в браузере."
                " Знания SQL, python. Опыт тестирования веб и/или...",
                "url": "https://api.hh.ru/vacancies/117253650?host=hh.ru",
            }
        ]
    }


@patch("src.headhunterapi.HeadHunterAPI._connect_to_api")
def test_get_vacancies(mock_connect_to_api):
    hh_2 = HeadHunterAPI()
    mock_connect_to_api.return_value = {"items": [{"name": "Python-Разработчик", "salary": {"from": 150000}}]}

    result = hh_2.get_vacancies("Разработчик")
    assert result == [
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
        {"name": "Python-Разработчик", "salary": {"from": 150000}},
    ]
