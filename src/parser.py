from abc import ABC, abstractmethod
from typing import Any


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def _connect_to_api(self) -> Any:
        """Абстрактный метод, который подключается к API."""
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs) -> list:
        """Абстрактный метод, который получает необходимые вакансии по ключевому слову."""
        pass
