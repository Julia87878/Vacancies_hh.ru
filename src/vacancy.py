from typing import Any, Union


class Vacancy:
    """Класс для работы с вакансиями."""

    __slots__ = ("__name", "__salary_from", "__snippet", "__url")

    def __init__(self, name: str, salary_from: Union[int, str], snippet: str, url: str) -> None:
        """Метод конструктор."""
        self.__name = self.__validate_name(name)
        self.__salary_from = self.__validate_salary(salary_from)
        self.__snippet = self.__validate_snippet(snippet)
        self.__url = self.__validate_url(url)

    @property
    def name(self) -> str:
        """Возвращает название вакансии."""
        return self.__name

    @property
    def salary_from(self) -> Any:
        """Возвращает минимальную зарплату."""
        return self.__salary_from

    @property
    def snippet(self) -> str:
        """Возвращает требования к соискателю."""
        return self.__snippet

    @property
    def url(self) -> str:
        """Возвращает ссылку на вакансию."""
        return self.__url

    def __str__(self) -> str:
        """Строковое отображение экземпляра вакансии."""
        return (
            f"Название вакансии: {self.name}, Зарплата: от {self.salary_from}, "
            f"Требования: {self.__snippet}, Ссылка на вакансию: {self.url}."
        )

    def __ge__(self, other) -> bool:
        """Метод сравнения вакансий по заработной плате(больше или равно)."""
        if isinstance(other, Vacancy):
            return self.salary_from >= other.salary_from
        else:
            return NotImplemented

    def __gt__(self, other) -> bool:
        """Метод сравнения вакансий по заработной плате(больше)."""
        if isinstance(other, Vacancy):
            return self.salary_from > other.salary_from
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        """Метод сравнения вакансий по заработной плате(меньше или равно)."""
        if isinstance(other, Vacancy):
            return self.salary_from <= other.salary_from
        else:
            return NotImplemented

    def __lt__(self, other) -> bool:
        """Метод сравнения вакансий по заработной плате(меньше)."""
        if isinstance(other, Vacancy):
            return self.salary_from < other.salary_from
        else:
            return NotImplemented

    @staticmethod
    def __validate_name(name: str) -> str:
        """Метод валидации названия вакансии."""
        if not name:
            return "Название вакансии не указано."
        return name

    @staticmethod
    def __validate_salary(salary: Union[int, str]) -> Any:
        """Метод валидации заработной платы."""
        if salary is None or (isinstance(salary, str)):
            return "Зарплата не указана."
        elif isinstance(salary, int) and salary < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        return salary

    @staticmethod
    def __validate_snippet(snippet: str) -> str:
        """Метод валидации требований к соискателю."""
        if not snippet:
            return "Требования к соискателю не указаны."
        return snippet

    @staticmethod
    def __validate_url(url: str) -> str:
        """Метод валидации ссылки на вакансию."""
        if not url:
            return "Ссылка на вакансию не указана."
        return url

    @classmethod
    def cast_to_object_list(cls, hh_api_vacancies: list) -> list:
        """Метод, который преобразует список вакансий в список объектов класса Vacancy."""
        object_vacancies = []
        for vacancy in hh_api_vacancies:
            salary_data = cls.__validate_salary(vacancy.get("salary", {}))
            if isinstance(salary_data, str):
                salary_from = "Зарплата не указана."
            else:
                salary_from = cls.__validate_salary(salary_data.get("from"))
            vacancy = Vacancy(
                name=vacancy.get("name", "Not specified"),
                salary_from=salary_from,
                snippet=vacancy.get("snippet", {}).get("requirement", "Not specified"),
                url=vacancy.get("url", "Not specified"),
            )

            object_vacancies.append(vacancy.to_dict())

        return object_vacancies

    def to_dict(self) -> dict:
        """Метод, который преобразует объект класса Vacancy в словарь для дальнейшей записи в JSON-файл"""

        return {
            "name": self.name,
            "salary_from": self.salary_from,
            "snippet": self.snippet,
            "url": self.url,
        }
