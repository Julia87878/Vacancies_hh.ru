from abc import ABC, abstractmethod


class BaseSaver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def get_data_from_file(self):
        """Абстрактный метод, который получает данные из файла."""
        pass

    @abstractmethod
    def add_data_in_file(self, vacancy_list: list):
        """Абстрактный метод, который добавляет данные в файл."""
        pass

    @abstractmethod
    def delete_data_from_file(self, vacancy_url: str):
        """Абстрактный метод, который удаляет данные из файла."""
        pass
