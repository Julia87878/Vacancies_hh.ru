import re

import pandas as pd


def get_vacancies_by_keyword(vacancies: list[dict], keyword: str) -> list:
    """Функция, которая фильтрует вакансии по ключевому слову."""
    filtered_vacancies = []
    for vacancy in vacancies:
        snippet_value = vacancy.get("snippet", "")
        if isinstance(snippet_value, str) and re.findall(keyword, snippet_value, flags=re.IGNORECASE):
            filtered_vacancies.append(vacancy)
    return filtered_vacancies


def get_vacancies_salary_from(salary: int, filtered_vacancies: list) -> list:
    """Функция, которая фильтрует вакансии по зарплате(от минимального размера зарплаты и выше)."""
    vacancies_salary_from = []
    for vacancy in filtered_vacancies:
        salary_from = vacancy.get("salary_from", 0)
        if isinstance(salary_from, str):
            salary_from = 0
        if salary_from >= salary:
            vacancies_salary_from.append(vacancy)
    return vacancies_salary_from


def get_top_n_vacancies(vacancies_salary_from: list, user_top_n: int) -> list:
    """Функция, которая получает топ N вакансий по минимальной зарплате."""
    sorted_salary = sorted(
        vacancies_salary_from,
        key=lambda i: (int(i.get("salary_from", 0)) if str(i.get("salary_from", 0)).isdigit() else 0),
        reverse=True,
    )
    df = pd.DataFrame(sorted_salary)
    if user_top_n > len(df):
        user_top_n = len(df)
    top_n_df = df.head(user_top_n)
    top_n_df_dict = top_n_df.to_dict(orient="records")
    return top_n_df_dict


def to_str(top_vacancies: list) -> str:
    """Функция, которая список словарей преобразует в строковое представление."""
    str_vacancies = []
    for vacancy in top_vacancies:
        name = vacancy.get("name", "")
        salary = vacancy.get("salary_from", 0)
        snippet = vacancy.get("snippet", "")
        url = vacancy.get("url", "")
        vac_str = (
            f"Название вакансии: {name}, Зарплата: от {salary}, Требования: {snippet}, Ссылка на вакансию: {url}."
        )
        str_vacancies.append(vac_str)
    result = " ".join(str_vacancies)
    return result
