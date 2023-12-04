import os

from utils import get_emploeers, get_vacancies, create_database, save_data_to_database
from config import config
from DBmanager import DBmanager


def main():
    url = "https://api.hh.ru"
    emploeer_ids = [1740, 15478, 8620, 3529, 78638, 64174, 84585, 633069, 1375441, 1122462]
    params = config()

    data_emploeers = get_emploeers(url, emploeer_ids)
    data_vacancies = get_vacancies(url, emploeer_ids)
    create_database('hh', params)
    save_data_to_database(data_emploeers, data_vacancies, 'hh', params)
    db = DBmanager('hh', params)

    EXIT = "0"
    COMPANIES_AND_VACANCIES = "1"
    ALL_VACANCIES = "2"
    AVG_SALARY = "3"
    VACANCIES_WITH_HIGHER_SALARY = "4"
    VACANCIES_WITH_KEYWORD = "5"

    while True:
        command = input(
            "Выберите действие программы: \n"
            "1 - получает список всех компаний и количество вакансий у каждой компании\n"
            "2 - получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n"
            "3 - получает среднюю зарплату по вакансиям\n"
            "4 - получает список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
            "5 - получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python\n"
            "0 - завершение работы\n"
        )

        if command == EXIT:
            break

        elif command == COMPANIES_AND_VACANCIES:
            print(db.get_companies_and_vacancies_count())

        elif command == ALL_VACANCIES:
            print(db.get_all_vacancies())

        elif command == AVG_SALARY:
            print(db.get_avg_salary())

        elif command == VACANCIES_WITH_HIGHER_SALARY:
            print(db.get_vacancies_with_higher_salary())

        elif command == VACANCIES_WITH_KEYWORD:
            keyword = input("Напишите запрос\n")
            print(db.get_vacancies_with_keyword(keyword))

        else:
            print("Неизвестная команда!")




if __name__ == '__main__':
    main()

