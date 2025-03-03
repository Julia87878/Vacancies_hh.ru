from src import settings
from src.headhunterapi import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.utils import get_top_n_vacancies, get_vacancies_by_keyword, get_vacancies_salary_from, to_str
from src.vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем."""
    search_query = input("Введите название интересующей вас вакансии: ")
    user_top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    keyword = input("Введите ключевое слово для фильтрации вакансий: ")
    salary = int(input("Какой минимальный размер зарплаты вы рассматриваете?: "))
    hh = HeadHunterAPI()
    hh_vacancies = hh.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(hh_vacancies)
    jsonsaver = JSONSaver(filepath=settings.BASE_DIR.joinpath("data", "vacancies.json"))
    jsonsaver.add_data_in_file(vacancies)
    vacancies_from_file = jsonsaver.get_data_from_file()
    filtered_vacancies = get_vacancies_by_keyword(vacancies_from_file, keyword)
    vacancies_salary_from = get_vacancies_salary_from(salary, filtered_vacancies)
    top_vacancies = get_top_n_vacancies(vacancies_salary_from, user_top_n)
    if len(top_vacancies) > 0:
        return to_str(top_vacancies)
    else:
        return "Вакансии по заданным параметрам не найдены."


if __name__ == "__main__":
    print(user_interaction())
