from typing import Any

import requests

from src.parser import Parser


class HeadHunterAPI(Parser):
    """Класс для работы с платформой hh.ru, подключается к API и получает вакансии."""

    def __init__(self) -> None:
        """Инициализирует класс HeadHunterAPI и задает начальные параметры."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 10}
        self.__vacancies: list = []

    def _connect_to_api(self) -> Any:
        """Метод, который подключается к API(HeadHunter)."""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code != 200:
            raise ValueError("Ошибка.")
        else:
            return response.json()

    def get_vacancies(self, keyword: str) -> list:
        """Получение вакансий по ключевому слову"""
        self.__params["text"] = keyword
        self.__params["per_page"] = 10

        while self.__params.get("page") != 10:
            response = self._connect_to_api()
            vacancies = response["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1
        return self.__vacancies
