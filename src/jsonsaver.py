import json
from pathlib import Path
from typing import Any

from src.basesaver import BaseSaver


class JSONSaver(BaseSaver):
    """Класс для работы  с JSON-файлами."""

    def __init__(self, filepath: Path, filename: str = "vacancies.json") -> None:
        """Метод конструктор."""
        self.filepath = filepath
        if not filepath.exists:
            raise FileNotFoundError("Файл не найден.")
        self.__filename = filename

    def get_data_from_file(self) -> Any:
        """Метод, который получает данные из файла."""
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except json.JSONDecodeError:
            return []

    def add_data_in_file(self, vacancy_list: list) -> None:
        """Метод, который добавляет данные в файл."""
        read_data = self.get_data_from_file()
        if not read_data:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(vacancy_list, f, ensure_ascii=False, indent=4)
        else:
            for vacancy in vacancy_list:
                if vacancy in read_data:
                    continue
                read_data.append(vacancy)
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(read_data, f, ensure_ascii=False, indent=4)

    def delete_data_from_file(self, vacancy_url: str) -> None:
        """Метод, который удаляет данные из файла."""
        read_data = self.get_data_from_file()
        read_data = [vacancy for vacancy in read_data if vacancy.get("url") != vacancy_url]
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(read_data, f, ensure_ascii=False, indent=4)
